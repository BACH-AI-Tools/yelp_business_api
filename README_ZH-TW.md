# Yelp Business Api MCP Server

[English](./README_EN.md) | [简体中文](./README.md) | 繁體中文

## 🚀 使用 EMCP 平台快速體驗

**[EMCP](https://sit-emcp.kaleido.guru)** 是一個強大的 MCP 伺服器管理平台，讓您無需手動配置即可快速使用各種 MCP 伺服器！

### 快速開始：

1. 🌐 造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)**
2. 📝 註冊並登入帳號
3. 🎯 進入 **MCP 廣場**，瀏覽所有可用的 MCP 伺服器
4. 🔍 搜尋或找到本伺服器（`bach-yelp_business_api`）
5. 🎉 點擊 **「安裝 MCP」** 按鈕
6. ✅ 完成！即可在您的應用中使用

### EMCP 平台優勢：

- ✨ **零配置**：無需手動編輯配置檔案
- 🎨 **視覺化管理**：圖形介面輕鬆管理所有 MCP 伺服器
- 🔐 **安全可靠**：統一管理 API 金鑰和認證資訊
- 🚀 **一鍵安裝**：MCP 廣場提供豐富的伺服器選擇
- 📊 **使用統計**：即時查看服務調用情況

立即造訪 **[EMCP 平台](https://sit-emcp.kaleido.guru)** 開始您的 MCP 之旅！


---

## 簡介

這是一個 MCP 伺服器，用於存取 Yelp Business Api API。

- **PyPI 套件名**: `bach-yelp_business_api`
- **版本**: 2.0.0
- **傳輸協定**: stdio


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

## 配置

### API 認證

此 API 需要認證。請設定環境變數:

```bash
export API_KEY="your_api_key_here"
```

### 環境變數

| 變數名 | 說明 | 必需 |
|--------|------|------|
| `API_KEY` | API 金鑰 | 是 |




### 在 Claude Desktop 中使用

编辑 Claude Desktop 配置文件 `claude_desktop_config.json`:


```json
{
  "mcpServers": {
    "yelp_business_api": {
      "command": "uvx",
      "args": ["--from", "bach-yelp_business_api", "bach_yelp_business_api"],
      "env": {
        "API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**: 請將 `E:\path\to\yelp_business_api\server.py` 替換為實際的伺服器檔案路徑。


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

- **传输协议**: stdio
- **HTTP 客户端**: httpx

## 开发

此伺服器由 [API-to-MCP](https://github.com/BACH-AI-Tools/api-to-mcp) 工具自動生成。

版本: 2.0.0
