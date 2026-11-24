"""Core Sandbox Marshaller implementation."""
import time
from typing import Dict, Any, Callable

class ExecutionResult:
    def __init__(self, success: bool, output: Any, execution_time_ms: float, error: str = ""):
        self.success = success
        self.output = output
        self.execution_time_ms = execution_time_ms
        self.error = error

class SandboxMarshaller:
    def __init__(self, timeout_ms: float = 1000.0, max_output_chars: int = 10000):
        self.timeout_ms = timeout_ms
        self.max_output_chars = max_output_chars

    def execute_safely(self, fn: Callable[..., Any], *args, **kwargs) -> ExecutionResult:
        start = time.time()
        try:
            res = fn(*args, **kwargs)
            duration = (time.time() - start) * 1000.0
            if duration > self.timeout_ms:
                return ExecutionResult(False, None, duration, f"Execution timed out ({duration:.1f}ms > {self.timeout_ms}ms)")

            out_str = str(res)
            if len(out_str) > self.max_output_chars:
                res = out_str[:self.max_output_chars] + "...[TRUNCATED]"

            return ExecutionResult(True, res, duration)
        except Exception as e:
            duration = (time.time() - start) * 1000.0
            return ExecutionResult(False, None, duration, f"Execution exception: {str(e)}")
