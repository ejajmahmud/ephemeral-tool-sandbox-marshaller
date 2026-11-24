"""CLI for Ephemeral Sandbox Marshaller."""
import argparse
from .core import SandboxMarshaller

def main():
    parser = argparse.ArgumentParser(description="Ephemeral Tool Sandbox Marshaller CLI")
    parser.add_argument("--demo", action="store_true", help="Run sandboxed execution demo")
    args = parser.parse_args()

    marshaller = SandboxMarshaller(timeout_ms=500.0)
    res = marshaller.execute_safely(lambda x: x ** 2, 42)
    print(f"Safe run result: {res.output} (Success: {res.success}, Time: {res.execution_time_ms:.2f}ms)")

if __name__ == "__main__":
    main()
