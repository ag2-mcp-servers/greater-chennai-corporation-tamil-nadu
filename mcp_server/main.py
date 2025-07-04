# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:55:18+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    BtcerCertificatePostRequest,
    BtcerCertificatePostResponse,
    BtcerCertificatePostResponse1,
    BtcerCertificatePostResponse2,
    BtcerCertificatePostResponse3,
    BtcerCertificatePostResponse4,
    BtcerCertificatePostResponse5,
    BtcerCertificatePostResponse6,
    DtcerCertificatePostRequest,
    DtcerCertificatePostResponse,
    DtcerCertificatePostResponse1,
    DtcerCertificatePostResponse2,
    DtcerCertificatePostResponse3,
    DtcerCertificatePostResponse4,
    DtcerCertificatePostResponse5,
    DtcerCertificatePostResponse6,
)

app = MCPProxy(
    description="Birth and Death certificates from 1934-till date, as provided by Greater Chennai Corporation (http://www.chennaicorporation.gov.in), can be downloaded in citizen's DigiLocker account.",
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Greater Chennai Corporation, Tamil Nadu',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/chennaicorp/v3'}],
)


@app.post(
    '/btcer/certificate',
    description=""" API to verify Birth Certificate. """,
    tags=['certificate_handling'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def btcer(body: BtcerCertificatePostRequest = None):
    """
    Birth Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/dtcer/certificate',
    description=""" API to verify Death Certificate. """,
    tags=['certificate_handling'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def dtcer(body: DtcerCertificatePostRequest = None):
    """
    Death Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
