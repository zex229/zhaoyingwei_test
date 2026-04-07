import httpx
import asyncio

# 同步示例
def sync_example():
    """同步发送 HTTP 请求示例"""
    print("=== 同步请求示例 ===")
    
    # 基本 GET 请求
    with httpx.Client() as client:
        response = client.get('https://httpbin.org/get')
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.json()}")
    
    # 带参数的 GET 请求
    with httpx.Client() as client:
        params = {'q': 'python', 'page': '1'}
        response = client.get('https://httpbin.org/get', params=params)
        print(f"\n带参数的请求 URL: {response.url}")
    
    # POST 请求
    with httpx.Client() as client:
        data = {'key1': 'value1', 'key2': 'value2'}
        response = client.post('https://httpbin.org/post', json=data)
        print(f"\nPOST 请求状态码: {response.status_code}")
    
    # 带请求头的请求
    with httpx.Client() as client:
        headers = {'User-Agent': 'httpx-example/1.0'}
        response = client.get('https://httpbin.org/headers', headers=headers)
        print(f"\n带请求头的响应: {response.json()}")


# 异步示例
async def async_example():
    """异步发送 HTTP 请求示例"""
    print("\n=== 异步请求示例 ===")
    
    # 基本异步 GET 请求
    async with httpx.AsyncClient() as client:
        response = await client.get('https://httpbin.org/get')
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.json()}")
    
    # 并发请求
    async with httpx.AsyncClient() as client:
        tasks = [
            client.get('https://httpbin.org/get'),
            client.get('https://httpbin.org/headers'),
            client.get('https://httpbin.org/ip')
        ]
        responses = await asyncio.gather(*tasks)
        
        print(f"\n并发请求完成，响应数量: {len(responses)}")
        for i, resp in enumerate(responses):
            print(f"请求 {i+1} 状态码: {resp.status_code}")


if __name__ == '__main__':
    # 运行同步示例
    sync_example()
    
    # 运行异步示例
    asyncio.run(async_example())
