# Yelp Business Api MCP Server

English | [简体中文](./README.md) | [繁體中文](./README_ZH-TW.md)

## 🚀 Quick Start with EMCP Platform

**[EMCP](https://sit-emcp.kaleido.guru)** is a powerful MCP server management platform that allows you to quickly use various MCP servers without manual configuration!

### Quick Start:

1. 🌐 Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)**
2. 📝 Register and login
3. 🎯 Go to **MCP Marketplace** to browse all available MCP servers
4. 🔍 Search or find this server (`bach-yelp_business_api`)
5. 🎉 Click the **"Install MCP"** button
6. ✅ Done! You can now use it in your applications

### EMCP Platform Advantages:

- ✨ **Zero Configuration**: No need to manually edit config files
- 🎨 **Visual Management**: Easy-to-use GUI for managing all MCP servers
- 🔐 **Secure & Reliable**: Centralized API key and authentication management
- 🚀 **One-Click Install**: Rich selection of servers in MCP Marketplace
- 📊 **Usage Statistics**: Real-time service call monitoring

Visit **[EMCP Platform](https://sit-emcp.kaleido.guru)** now to start your MCP journey!


---

## Introduction

This is an automatically generated MCP server using [FastMCP](https://fastmcp.wiki) for accessing the Yelp Business Api API.

- **PyPI Package**: `bach-yelp_business_api`
- **Version**: 1.0.0
- **Transport Protocol**: stdio


## 安装

### 从 PyPI 安装:

```bash
pip install bach-yelp_business_api
```

### 从源码安装:

```bash
pip install -e .
```

## 运行

### 方式 1: 使用 uvx（推荐，无需安装）

```bash
# 运行（uvx 会自动安装并运行）
uvx --from bach-yelp_business_api bach_yelp_business_api

# 或指定版本
uvx --from bach-yelp_business_api@latest bach_yelp_business_api
```

### 方式 2: 直接运行（开发模式）

```bash
python server.py
```

### 方式 3: 安装后作为命令运行

```bash
# 安装
pip install bach-yelp_business_api

# 运行（命令名使用下划线）
bach_yelp_business_api
```

## Configuration

### API Authentication

This API requires authentication. Please set environment variable:

```bash
export API_KEY="your_api_key_here"
```

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | API Key | Yes |




### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "yelp_business_api": {
      "command": "python",
      "args": ["E:\path\to\yelp_business_api\server.py"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**Note**: Replace `E:\path\to\yelp_business_api\server.py` with the actual server file path.


## 可用工具

此服务器提供以下工具:


### `__reviews`

Get business reviews by url or id

**端点**: `GET /reviews`


**参数**:

- `business_url` (string): Enter any business url from yelp.com (any subdomain)

- `business_id` (string): Enter any business ID found from /search endpoint

- `reviews_per_page` (string): Max value could be: 45

- `end_cursor` (string): For first page: Default is set to None For next pages, if hasNextPage = true : Input the end_cursor value found from the response of the previous page to get reviews of the next page. Ex. end_cursor = eyJ2ZXJzaW9uIjoxLCJ0eXBlIjoib2Zmc2V0Iiwib2Zmc2V0Ijo0NH0

- `sort_by` (string): Example value: 

- `rating_filter` (string): Example value: 



---


### `___search_yelp_category`

Select any category you want to scrape.

**端点**: `GET /search/category`


**参数**:

- `location` (string) *必需*: Example value: New York, NY

- `search_category` (string) *必需*: Search for any category available on Yelp. Ex. Restaurants, Pharmacy & Chemists, Animal Assisted Therapy, Dentists Few terms are not available as category searches, use term search. Ex. Movers, Plumbers

- `limit` (string): Number of results per page. Max: 40 Default: 10.

- `offset` (string): If offset is set to 0, it means start from zero. If offset is set to 20, it means to start showing after 20 results.

- `business_details_type` (string): Basic: provides basic info's about the businesses. Advanced: provides in-depth information about the businesses (it's like using /search and /each business details endpoints at the same time) Advanced option costs 2 requests per call.



---


### `__popular_dishes`

Get popular_dish list of a restaurant when available on the website.

**端点**: `GET /popular_dish`


**参数**:

- `business_id` (string) *必需*: Get popular dishes from a restaurant when available on the website. Input business_id.



---


### `__get_menus_beta`

Get restaurant menus if present on yelp

**端点**: `GET /get_menus`


**参数**:

- `business_id` (string) *必需*: Find restaurant menus if present on the Yelp website. Menus on personal websites cannot be collected.



---


### `_business_url_to_id`

Find biz id from url.

**端点**: `GET /biz_url2id`


**参数**:

- `business_url` (string) *必需*: Enter url to find the business id.



---


### `___search_yelp_term`

Use the same search box on yelp.com

**端点**: `GET /search`


**参数**:

- `location` (string) *必需*: Enter exact locations. For example, use Roosevelt, NY not Roosevelt only.

- `search_term` (string) *必需*: Enter any search term you want, just like on Yelp. Ex. Coffee shop, Pizza shop, electrician, or plumber Ex. Black Owned Saloon, Mexican pizza shop

- `limit` (string): Number of results per page. Max: 40 Default: 10.

- `offset` (string): If offset is set to 0, it means start from zero. If offset is set to 20, it means to start showing after 20 results.

- `business_details_type` (string): Basic: provides basic info's about the businesses. Advanced: provides in-depth information about the businesses (it's like using /search and /each business details endpoints at the same time) Advanced option costs 2 requests per call.



---


### `__business_details`

Scrape By Yelp URL: Ex. https://www.yelp.com/biz/capital-blossom-day-spa-washington  or by business ids found from /search endpoint.  You can get these business urls from the \

**端点**: `GET /each`


**参数**:

- `business_url` (string): Get the business details by Yelp Business URL.

- `business_ids` (string): Get business details from business_id found from /search endpoint. Separate each using a comma. You can put up to 39 business ids on each request. Ex. BCUhfgjbVVvjs0ro4ATRsg,wj7ekipyvssV3Ok7p8zxGg, V2_qfjnwAVWqIphf7y866w



---


### `_upcheck`

Check if the api status is live!

**端点**: `GET /upcheck`


**参数**:

- `check` (string) *必需*: Example value: true



---



## 技术栈

- **FastMCP**: 快速、Pythonic 的 MCP 服务器框架
- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

This server is automatically generated by [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) tool.

Version: 1.0.0
