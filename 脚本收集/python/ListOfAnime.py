import requests
import json
import time

cookies = {
    'buvid3': 'B9A11397-3D41-FDEE-D79A-B26145386D1D82068infoc',
    'b_nut': '1758365182',
    'theme_style': 'dark',
    'buvid4': 'EDEA8691-961B-E128-5D0E-2F80F39489A589029-025092018-HoVLb0upfKQisfLPA6vzcA%3D%3D',
    'enable_web_push': 'DISABLE',
    'home_feed_column': '5',
    'browser_resolution': '2356-1352',
    'CURRENT_FNVAL': '4048',
    'rpdid': "|(J|k~lkY~uY0J'u~l)l|YYYJ",
    'SESSDATA': '72d51a43%2C1774093358%2Ce6d76%2A92CjD7oPTSeD69fC_VbEEQUnWiPxNyluGdHsNqDHpzFwKY9JDDoR_QHc50pfqHCMIxJlUSVmZ2X05TUXFkU2NYdHFsUFppT1REQWc4YUNDdVBTVDhhU185QjFlX0l6VnhpazRyeFVMUlM0dnRGT1kyenBxcXZsWnhwT3prdmFMcVNTSkJHam42YlF3IIEC',
    'bili_jct': '0223667e5405c2a4d04cb48ec66d3b07',
    'DedeUserID': '286063998',
    'DedeUserID__ckMd5': 'c0c341b6f04672c4',
    'theme-tip-show': 'SHOWED',
    'LIVE_BUVID': 'AUTO9317587968097691',
    'bp_t_offset_286063998': '1123153219422257152',
    'theme-avatar-tip-show': 'SHOWED',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjA0MzQ0OTgsImlhdCI6MTc2MDE3NTIzOCwicGx0IjotMX0.h_vaAU9nyvWP_ZN1o9jSrOWsXm4spd2prJC-zzxc4CI',
    'bili_ticket_expires': '1760434438',
    'CURRENT_QUALITY': '80',
    'buvid_fp': '524237dd36b3490a5518da3ba5a3e110',
    '_uuid': '9C8947C4-B10FC-8B55-D1069-766DC10953C6983179infoc',
    'theme-switch-show': 'SHOWED',
    'sid': '5xp5fw1c',
    'timeMachine': '0',
    'b_lsid': 'CA88FE9E_199E10EFABD',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,zh-CN;q=0.7,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Cookie': "buvid3=B9A11397-3D41-FDEE-D79A-B26145386D1D82068infoc; b_nut=1758365182; theme_style=dark; buvid4=EDEA8691-961B-E128-5D0E-2F80F39489A589029-025092018-HoVLb0upfKQisfLPA6vzcA%3D%3D; enable_web_push=DISABLE; home_feed_column=5; browser_resolution=2356-1352; CURRENT_FNVAL=4048; rpdid=|(J|k~lkY~uY0J'u~l)l|YYYJ; SESSDATA=72d51a43%2C1774093358%2Ce6d76%2A92CjD7oPTSeD69fC_VbEEQUnWiPxNyluGdHsNqDHpzFwKY9JDDoR_QHc50pfqHCMIxJlUSVmZ2X05TUXFkU2NYdHFsUFppT1REQWc4YUNDdVBTVDhhU185QjFlX0l6VnhpazRyeFVMUlM0dnRGT1kyenBxcXZsWnhwT3prdmFMcVNTSkJHam42YlF3IIEC; bili_jct=0223667e5405c2a4d04cb48ec66d3b07; DedeUserID=286063998; DedeUserID__ckMd5=c0c341b6f04672c4; theme-tip-show=SHOWED; LIVE_BUVID=AUTO9317587968097691; bp_t_offset_286063998=1123153219422257152; theme-avatar-tip-show=SHOWED; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjA0MzQ0OTgsImlhdCI6MTc2MDE3NTIzOCwicGx0IjotMX0.h_vaAU9nyvWP_ZN1o9jSrOWsXm4spd2prJC-zzxc4CI; bili_ticket_expires=1760434438; CURRENT_QUALITY=80; buvid_fp=524237dd36b3490a5518da3ba5a3e110; _uuid=9C8947C4-B10FC-8B55-D1069-766DC10953C6983179infoc; theme-switch-show=SHOWED; sid=5xp5fw1c; timeMachine=0; b_lsid=CA88FE9E_199E10EFABD",
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=0, i',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

base_params = {
    'vmid': '97257656',
    'type': '1',
    'ps': '24',
    'playform': 'web',
    'follow_status': '0',
    'web_location': '333.1387',
    'w_rid': 'cc6854bed0869fff9632f1b86db2e7b2',
    'wts': '1760417586',
}

all_bangumi_list = []
total_count = 0
current_page = 1

print("开始获取追番列表...")

while True:
    # 为当前页设置参数
    params = base_params.copy()
    params['pn'] = str(current_page)
    
    print(f"正在获取第 {current_page} 页...")
    
    try:
        response = requests.get('https://api.bilibili.com/x/space/bangumi/follow/list', params=params, cookies=cookies, headers=headers)
        
        print(f"第 {current_page} 页响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            # 检查API返回的状态
            if data.get('code') == 0:
                page_bangumi_list = data.get('data', {}).get('list', [])
                page_total = data.get('data', {}).get('total', 0)
                
                if current_page == 1:
                    total_count = page_total
                    print(f"总共有 {total_count} 部追番")
                
                if not page_bangumi_list:
                    print(f"第 {current_page} 页没有更多数据，获取完成")
                    break
                
                all_bangumi_list.extend(page_bangumi_list)
                print(f"第 {current_page} 页获取到 {len(page_bangumi_list)} 部番剧")
                
                current_page += 1
                
                # 添加短暂延迟避免请求过快
                import time
                time.sleep(0.5)
                
            else:
                print(f"第 {current_page} 页API返回错误: {data.get('message', '未知错误')}")
                print(f"错误码: {data.get('code', 'N/A')}")
                break
        else:
            print(f"第 {current_page} 页HTTP请求失败: {response.status_code}")
            print(f"响应内容: {response.text}")
            break

    except requests.exceptions.RequestException as e:
        print(f"第 {current_page} 页请求异常: {e}")
        break
    except json.JSONDecodeError as e:
        print(f"第 {current_page} 页JSON解析错误: {e}")
        break
    except Exception as e:
        print(f"第 {current_page} 页未知错误: {e}")
        break

print(f"\n数据获取完成！")
print(f"实际获取到 {len(all_bangumi_list)} 部追番 (总计应有 {total_count} 部)")
print("=" * 60)

# 解析并显示所有追番信息
for i, bangumi in enumerate(all_bangumi_list, 1):
    title = bangumi.get('title', '未知标题')
    season_id = bangumi.get('season_id', 'N/A')
    media_id = bangumi.get('media_id', 'N/A')
    url = bangumi.get('url', 'N/A')
    cover = bangumi.get('cover', 'N/A')
    new_ep = bangumi.get('new_ep', {})
    areas = bangumi.get('areas', [])
    areas_str = ', '.join([area.get('name', '') for area in areas])
    rating = bangumi.get('rating', {})
    rating_str = f"{rating.get('score', 'N/A')}" if rating else 'N/A'
    
    print(f"{i}. {title}")
    print(f"   Season ID: {season_id}")
    print(f"   Media ID: {media_id}")
    print(f"   地区: {areas_str}")
    print(f"   评分: {rating_str}")
    print(f"   链接: {url}")
    print(f"   封面: {cover}")
    
    if new_ep:
        index_show = new_ep.get('index_show', 'N/A')
        print(f"   最新一集: {index_show}")
    
    print("-" * 40)

# 保存完整数据到JSON文件
complete_data = {
    'total': total_count,
    'actual_count': len(all_bangumi_list),
    'fetch_time': '2025-10-14',
    'bangumi_list': all_bangumi_list
}

with open("complete_bangumi_list.json", "w", encoding="utf-8") as f:
    json.dump(complete_data, f, ensure_ascii=False, indent=2)
print(f"\n完整数据已保存到 complete_bangumi_list.json")

# 保存简化版本到txt文件
with open("complete_bangumi_list.txt", "w", encoding="utf-8") as f:
    f.write(f"完整追番列表 (获取到 {len(all_bangumi_list)} / {total_count} 部)\n")
    f.write("=" * 60 + "\n\n")
    
    for i, bangumi in enumerate(all_bangumi_list, 1):
        title = bangumi.get('title', '未知标题')
        areas = bangumi.get('areas', [])
        areas_str = ', '.join([area.get('name', '') for area in areas])
        rating = bangumi.get('rating', {})
        rating_str = f" - 评分: {rating.get('score', 'N/A')}" if rating else ''
        new_ep = bangumi.get('new_ep', {})
        ep_info = f" - {new_ep.get('index_show', '')}" if new_ep.get('index_show') else ''
        
        f.write(f"{i}. {title} ({areas_str}){rating_str}{ep_info}\n")
        f.write(f"   链接: {bangumi.get('url', 'N/A')}\n\n")

print(f"简化列表已保存到 complete_bangumi_list.txt")

# 按地区统计
region_stats = {}
for bangumi in all_bangumi_list:
    areas = bangumi.get('areas', [])
    for area in areas:
        region_name = area.get('name', '未知')
        region_stats[region_name] = region_stats.get(region_name, 0) + 1

print(f"\n按地区统计:")
print("-" * 30)
for region, count in sorted(region_stats.items(), key=lambda x: x[1], reverse=True):
    print(f"{region}: {count} 部")

print(f"\n统计信息已保存到文件中。")

print("脚本执行完成")