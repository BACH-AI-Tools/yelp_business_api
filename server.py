"""
Yelp Business Api MCP Server

使用 FastMCP 的 from_openapi 方法自动生成

Version: 1.0.0
Transport: stdio
"""
import os
import json
import httpx
from fastmcp import FastMCP

# 服务器版本和配置
__version__ = "1.0.0"
__tag__ = "yelp_business_api/1.0.0"

# API 配置
API_KEY = os.getenv("API_KEY", "")

# 传输协议配置
TRANSPORT = "stdio"


# OpenAPI 规范
OPENAPI_SPEC = """{\n  \"openapi\": \"3.0.0\",\n  \"info\": {\n    \"title\": \"Yelp Business Api\",\n    \"version\": \"1.0.0\",\n    \"description\": \"RapidAPI: oneapiproject/yelp-business-api\"\n  },\n  \"servers\": [\n    {\n      \"url\": \"https://yelp-business-api.p.rapidapi.com\"\n    }\n  ],\n  \"paths\": {\n    \"/reviews\": {\n      \"get\": {\n        \"summary\": \"☑️ / Reviews\",\n        \"description\": \"Get business reviews by url or id\",\n        \"operationId\": \"☑️_/_reviews\",\n        \"parameters\": [\n          {\n            \"name\": \"business_url\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Enter any business url from yelp.com (any subdomain)\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"business_id\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Enter any business ID found from /search endpoint\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"reviews_per_page\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Max value could be: 45\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"20\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"end_cursor\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"For first page: Default is set to None For next pages, if hasNextPage = true : Input the end_cursor value found from the response of the previous page to get reviews of the next page. Ex. end_cursor = eyJ2ZXJzaW9uIjoxLCJ0eXBlIjoib2Zmc2V0Iiwib2Zmc2V0Ijo0NH0\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"sort_by\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"rating_filter\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Example value: \",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search/category\": {\n      \"get\": {\n        \"summary\": \"🔍  / Search Yelp (category)\",\n        \"description\": \"Select any category you want to scrape.\",\n        \"operationId\": \"🔍__/_search_yelp_(category)\",\n        \"parameters\": [\n          {\n            \"name\": \"location\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: New York, NY\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"search_category\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Search for any category available on Yelp. Ex. Restaurants, Pharmacy & Chemists, Animal Assisted Therapy, Dentists Few terms are not available as category searches, use term search. Ex. Movers, Plumbers\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of results per page. Max: 40 Default: 10.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"offset\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If offset is set to 0, it means start from zero. If offset is set to 20, it means to start showing after 20 results.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"business_details_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Basic: provides basic info's about the businesses. Advanced: provides in-depth information about the businesses (it's like using /search and /each business details endpoints at the same time) Advanced option costs 2 requests per call.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/popular_dish\": {\n      \"get\": {\n        \"summary\": \"🔝 / popular_dishes\",\n        \"description\": \"Get popular_dish list of a restaurant when available on the website.\",\n        \"operationId\": \"🔝_/_popular_dishes\",\n        \"parameters\": [\n          {\n            \"name\": \"business_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Get popular dishes from a restaurant when available on the website. Input business_id.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/get_menus\": {\n      \"get\": {\n        \"summary\": \"🌮 / Get Menus (beta)\",\n        \"description\": \"Get restaurant menus if present on yelp\",\n        \"operationId\": \"🌮_/_get_menus_(beta)\",\n        \"parameters\": [\n          {\n            \"name\": \"business_id\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Find restaurant menus if present on the Yelp website. Menus on personal websites cannot be collected.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/biz_url2id\": {\n      \"get\": {\n        \"summary\": \"/ Business URL to ID\",\n        \"description\": \"Find biz id from url.\",\n        \"operationId\": \"/_business_url_to_id\",\n        \"parameters\": [\n          {\n            \"name\": \"business_url\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter url to find the business id.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/search\": {\n      \"get\": {\n        \"summary\": \"🔍  / Search Yelp (term)\",\n        \"description\": \"Use the same search box on yelp.com\",\n        \"operationId\": \"🔍__/_search_yelp_(term)\",\n        \"parameters\": [\n          {\n            \"name\": \"location\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter exact locations. For example, use Roosevelt, NY not Roosevelt only.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"search_term\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Enter any search term you want, just like on Yelp. Ex. Coffee shop, Pizza shop, electrician, or plumber Ex. Black Owned Saloon, Mexican pizza shop\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"limit\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Number of results per page. Max: 40 Default: 10.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"10\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"offset\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"If offset is set to 0, it means start from zero. If offset is set to 20, it means to start showing after 20 results.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": \"0\",\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"business_details_type\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Basic: provides basic info's about the businesses. Advanced: provides in-depth information about the businesses (it's like using /search and /each business details endpoints at the same time) Advanced option costs 2 requests per call.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/each\": {\n      \"get\": {\n        \"summary\": \"📚 / Business details\",\n        \"description\": \"Scrape By Yelp URL: Ex. https://www.yelp.com/biz/capital-blossom-day-spa-washington  or by business ids found from /search endpoint.  You can get these business urls from the \\\\\",\n        \"operationId\": \"📚_/_business_details\",\n        \"parameters\": [\n          {\n            \"name\": \"business_url\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Get the business details by Yelp Business URL.\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          },\n          {\n            \"name\": \"business_ids\",\n            \"in\": \"query\",\n            \"required\": false,\n            \"description\": \"Get business details from business_id found from /search endpoint. Separate each using a comma. You can put up to 39 business ids on each request. Ex. BCUhfgjbVVvjs0ro4ATRsg,wj7ekipyvssV3Ok7p8zxGg, V2_qfjnwAVWqIphf7y866w\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    },\n    \"/upcheck\": {\n      \"get\": {\n        \"summary\": \"/ Upcheck\",\n        \"description\": \"Check if the api status is live!\",\n        \"operationId\": \"/_upcheck\",\n        \"parameters\": [\n          {\n            \"name\": \"check\",\n            \"in\": \"query\",\n            \"required\": true,\n            \"description\": \"Example value: true\",\n            \"schema\": {\n              \"type\": \"string\",\n              \"default\": null,\n              \"enum\": null\n            }\n          }\n        ],\n        \"responses\": {\n          \"200\": {\n            \"description\": \"Successful response\",\n            \"content\": {\n              \"application/json\": {\n                \"schema\": {}\n              }\n            }\n          }\n        }\n      }\n    }\n  },\n  \"components\": {\n    \"securitySchemes\": {\n      \"ApiAuth\": {\n        \"type\": \"apiKey\",\n        \"in\": \"header\",\n        \"name\": \"X-RapidAPI-Key\"\n      }\n    }\n  },\n  \"security\": [\n    {\n      \"ApiAuth\": []\n    }\n  ]\n}"""

# 创建 HTTP 客户端
# 设置默认 headers
default_headers = {}


# RapidAPI 必需的 headers
if API_KEY:
    default_headers["X-RapidAPI-Key"] = API_KEY
    default_headers["X-RapidAPI-Host"] = "yelp-business-api.p.rapidapi.com"
else:
    print("⚠️  警告: 未设置 API_KEY 环境变量")
    print("   RapidAPI 需要 API Key 才能正常工作")
    print("   请设置: export API_KEY=你的RapidAPI-Key")

# 对于 POST/PUT/PATCH 请求，自动添加 Content-Type
default_headers["Content-Type"] = "application/json"




client = httpx.AsyncClient(
    base_url="https://yelp-business-api.p.rapidapi.com", 
    timeout=30.0
)


# 从 OpenAPI 规范创建 FastMCP 服务器
openapi_dict = json.loads(OPENAPI_SPEC)
mcp = FastMCP.from_openapi(
    openapi_spec=openapi_dict,
    client=client,
    name="yelp_business_api",
    version=__version__
)


# 注册请求拦截器，为所有请求添加 RapidAPI headers
_original_request = client.request

async def _add_rapidapi_headers(method, url, **kwargs):
    """拦截所有请求，添加必需的 RapidAPI headers"""
    # 确保 headers 存在
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    
    # 添加 RapidAPI 必需的 headers
    if API_KEY:
        kwargs['headers']['X-RapidAPI-Key'] = API_KEY
        kwargs['headers']['X-RapidAPI-Host'] = "yelp-business-api.p.rapidapi.com"
    else:
        print("⚠️  警告: API_KEY 未设置，请求可能失败")
    
    # 对于 POST/PUT/PATCH，添加 Content-Type
    if method.upper() in ['POST', 'PUT', 'PATCH']:
        if 'Content-Type' not in kwargs['headers']:
            kwargs['headers']['Content-Type'] = 'application/json'
    
    return await _original_request(method, url, **kwargs)

# 替换 request 方法
client.request = _add_rapidapi_headers


def main():
    """主入口点"""
    print(f"🚀 启动 Yelp Business Api MCP 服务器")
    print(f"📦 版本: {__tag__}")
    print(f"🔧 传输协议: {TRANSPORT}")
    
    print()
    
    # 运行服务器
    
    mcp.run(transport="stdio")
    


if __name__ == "__main__":
    main()