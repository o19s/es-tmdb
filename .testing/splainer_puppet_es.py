import asyncio
from pyppeteer import launch

import re
import requests
import pandas as pd

file = 'splainer_links_es.csv'
dat = pd.read_csv(file)
codes = []

async def main():
    browser = await launch()

    for url in dat["URL"]:
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'networkidle0'})

        es_message = await page.querySelector('pre.ng-binding')
        content = await page.evaluate('element => element.textContent', es_message)
        code = re.findall("HTTP Error: ([0-9]+) .*", content)

        if len(code) == 0:
            codes.append('200')
        else:
            codes.append(code[0])
        
    await browser.close()

    dat["Code"] = codes
    dat.to_csv(file, index=False)
    print(f"{sum([x != '200' for x in codes])} of {len(codes)} of splainer links failed.")

asyncio.get_event_loop().run_until_complete(main())
