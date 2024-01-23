import requests
import json

headers = {
    'authority': 'svc-center-ext-tlt-corp-prod-service.talaadthai.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,en-US;q=0.9,th;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': '_clck=17mkwrb%7C2%7Cfim%7C0%7C1482; g-recapcha-result=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWNjZXNzIjp0cnVlLCJzY29yZSI6MSwiY3JlYXRlZEF0IjoiTW9uIEphbiAyMiAyMDI0IDEzOjM1OjU1IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSkiLCJpYXQiOjE3MDU5MzA1NTV9.WjJgu7_EqVkZ5rdCBIYjG63AM8yt6kpvvw0wEoCWUfI; _clsk=1njw0iv%7C1705930555330%7C1%7C1%7Cr.clarity.ms%2Fcollect',
    'origin': 'https://talaadthai.com',
    'pragma': 'no-cache',
    'referer': 'https://talaadthai.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-custom-recapcha-token': '03AFcWeA6IVuKV5UVesAjwyHFgPx3_Frf6q6kBUQuNGq5AYRfCluaaBUoX38jfogaZaOcDZvJkoOUAUogl_gCB8cCCsM0nxkXnW7fyTd3a7dmSL8H74Q4V2g1TVT2XPfTukyHIPXTvT71OhZ68IoksiTpi9-NpBB3ikNPmz6SR9bAGIpyGvnYluRYZpbGnqHw84O2SesHea2pztEoUI-qvHGGBbj5F46-Ix89z_8Cp8GTuVfiahWr5aRtBwRrIFkmKjgMyiSQNzamdUYQ_cWRNMUdvq2OXOahffMdS8g8sRKLPo-Jv4m584pa_GOpBte-2bEYjvRkDzGR7LiOUYZsKwLFGld5hglwSi_fMIzvbQGL-MaAtNIMYgSC1MYM9D23cWZEcolzvZDwmv0RB-BsMcUdKbni8fkgKrePuU8C86qDeBYoNT8u55y_a2R4dNm1Kwm_enbRrMBnoP6wKG29sKpdPNtNMzn_4VYGxZHDKy6GWEVaS2ATBUCrSxjEUGw08rTigCBYIvZJ6Zbnaz314994L5xEsRBNPuMry_4a6scGXyXsSzdmJ5I6EDtJ1cB1-wknPsTVeN2r69aK2oUU9fqMpZdCAIUqb0SqwraQkxy92uoDn2VBmEsBNmpidjjy9DEMWgY9ijWxCEdNAcy5GOfAWaXW9kPOnYdEHWzx4fvnDvQC5f8T-GOI2fYlxjMpV6Hs2s0THZcS6I9uHfW8czNl6h3ghd4uMtkJslqmjsp22RUabVUyau7smZSM_ev58lfYeJhyR7T9Z-hzO5A0A9jsYu-ZT6RZKcgU6Lbz9d__vNvj0QFWn_-j_68sjf9I94Pl0T4cjEJq1OkMXH1bdv09NGS1byK0ZCQDIVZSZbgEJK4UxaaVcQqwsUcDeAMovfHhRFNhgocVQwHxdYJPagjT2iivcB3lwgbhAzEYkF8Yb3b9lEJ0FIXAEvQmMdAEkBRHqXuyEQ_YZOftBNgLvi-sWwBAltACE2i9X1TPo1tpdn7vBgivGJmJMm3q3JH_aRYV2w0FdKiOVopSv8aLjODdDlcdWnWTA5-BMUY9ajQFhFGss8SXJnZ_M5bghvdyqa_-66fn18zi8t95naVzKWIITcupQDZjsvciEVg4GeeDNVVc3Otz8dOtt7a5OuD5TwfqI7-59w3PdD7ycXF0d9YHtM9CvmKnuJZx-FqUXlPtDNMcvwCp1NlivLULYhW92C84TBy3jXUMvA5deR_5iZDulqn9KipqXo4Ks321iPUoV8cRC-yfZ69JUm2-WZt-d6XYpWQr07mFYXl4QfsnpvFt2wsy184TZl6PwHwF1sS4duRxyaZsLADckfQYUNb4TSTKQyDcTGM7xMSnMkUFDhlXf52_gcEauVKs54vywXSBYACpZ169x32-ALuNt0OC1C5cbHkjN_JzOyWtPcI4U-m0n6l5eiUj6Nt2fd3iIpQeyTlQi9YTGKjeHxULwx0FBPmQU6ynoVqRQFniXRviu5fiD3bVbmkjXV0RS9mgXkKvav1dhy5UhWcxxrq43pMlHCLVQFP-4ZK_aJAN9FnGi9X2ziZ07ixxVcg',
}

params = {
    'productId': '1058',
    'dateFrom': '1674308165000',
    'dateTo': '1705930560000',
    'sumBy': 'month',
}

response = requests.get(
    'https://svc-center-ext-tlt-corp-prod-service.talaadthai.com/v1/ext/product/ProductPricingGraphSummary',
    params=params,
    # cookies=cookies,
    headers=headers,
)

if response.status_code == 200:
	data = response.json()
	with open('data.json', 'w') as f:
		json.dump(data, f)
else:
	print("Error:", response.status_code)
