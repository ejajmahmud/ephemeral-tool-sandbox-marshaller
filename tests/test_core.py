"""Tests for SandboxMarshaller."""
import unittest
from ephemeral_tool_sandbox_marshaller.core import SandboxMarshaller

class TestSandboxMarshaller(unittest.TestCase):
    def test_safe_execution(self):
        m = SandboxMarshaller()
        r = m.execute_safely(lambda a, b: a + b, 10, 20)
        self.assertTrue(r.success)
        self.assertEqual(r.output, 30)

    def test_exception_containment(self):
        m = SandboxMarshaller()
        r = m.execute_safely(lambda: 1 / 0)
        self.assertFalse(r.success)
        self.assertIn("division by zero", r.error)
