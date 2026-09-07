"""
Demonstration of Autonomous OpenAPI Tool Generator Skill
"""

from client import OpenAPIToolGenerator

def main():
    print("=== Compiling OpenAPI 3.0 Specification into Agent Tools ===")
    generator = OpenAPIToolGenerator()

    sample_openapi = {
        "openapi": "3.0.0",
        "info": {"title": "Payment API", "version": "1.0"},
        "paths": {
            "/payments/charge": {
                "post": {
                    "operationId": "create_charge",
                    "summary": "Create a credit card payment charge",
                    "parameters": [
                        {"name": "amount", "in": "body", "required": True, "type": "number"},
                        {"name": "currency", "in": "body", "required": True, "type": "string"},
                        {"name": "customer_id", "in": "body", "required": False, "type": "string"}
                    ]
                }
            },
            "/payments/refund": {
                "post": {
                    "operationId": "refund_charge",
                    "summary": "Refund an existing payment charge",
                    "parameters": [
                        {"name": "charge_id", "in": "body", "required": True, "type": "string"}
                    ]
                }
            }
        }
    }

    count = generator.parse_spec(sample_openapi)
    print(f"Successfully compiled {count} tools from OpenAPI spec:")
    for t_name, tool in generator.tools.items():
        print(f"  - Tool: {t_name} [{tool.method} {tool.path}] -> {tool.description}")

    print("\nExecuting tool 'create_charge':")
    res = generator.execute_tool_call("create_charge", amount=49.99, currency="USD", customer_id="cust_123")
    print("Execution Result:", res)

    assert res["status"] == "success"
    print("Autonomous OpenAPI Tool Generator Verification PASS!")

if __name__ == "__main__":
    main()
