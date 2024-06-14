import requests
import json
import requests

# for each run of this script, change url, header, json name, and for loop termination

payload = {}

headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcxODM1NjU0OS4zNjM5NDQsImlhdCI6MTcxODM1NTk0OS4zNjM5NDQsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzE4MzI0MDkwLjk3NTY4OTIsIFwicHJvZmlsZUlkXCI6IFwiby90T0VTbUxmZnd4cXgxc0dYSGJWaVVEc3JjMVFvU3VIdnZiemZjVHlHYkZuaitFMlJKQThBMm1xY3Q2cTZIcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTRlMDQ2NDU4ZGQ5MTU1NmE5MDAwYjI2OGFlMGM1ODZiOTc5Mjc2ZjA1NmQyZDQ4OTc3ZTljNWYxOGY2YTMwZDhcIiwgXCJhbm9ueW1vdXNcIjogdHJ1ZSwgXCJ0cmFjZXJcIjogXCJURFAwRTRUTTZNXCIsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwic2l0ZUlkXCI6IFwidW8tdXNcIiwgXCJicmFuZElkXCI6IFwidW9cIiwgXCJzaXRlR3JvdXBcIjogXCJ1by11c1wiLCBcImRhdGFDZW50ZXJJZFwiOiBcIlVTLVBBXCIsIFwiZ2VvUmVnaW9uXCI6IFwiVVMtUEFcIiwgXCJlZGdlc2NhcGVcIjoge1wicmVnaW9uQ29kZVwiOiBcIk5KXCJ9LCBcImNhcnRJZFwiOiBcIlo0MjlSbXNjSnMyZFQ0TDNONkU4N3hadEh4RmVNby9abVRmQUJqL3pBaVBwY25HRmJPck1tcVlJN3RVeGFNeUk1VSszcnMycnhoam00cEQzMENjSUJ3PT04MmI2MWMzOThlMDNlZGNmODBhN2FlMDYzYWZhY2M4ZmM1OTZmY2RhNTg2Yjg4MGExZmJiMTA1NTY3ZWQxZDhhXCJ9In0.TyclGNWHVP6H6l8IHjODrpzDYBO0K0CDSdvt5mDAk7Q',
  'cookie': 'SSLB=1; urbn_data_center_id=US-PA; urbn_geo_region=US-PA; urbn_tracer=TDP0E4TM6M; urbn_uuid=412027e6-061d-4078-9519-74ffacf4114e; urbn_clear=true; _pxvid=1dfb2a60-29e3-11ef-9aff-6dcc8f6f2ee7; utag_main_v_id=01901418dca0001d2271b885b1330506f0162067008df; _gid=GA1.2.787889430.1718324092; _gac_UA-45103817-1=1.1718324092.Cj0KCQjwsaqzBhDdARIsAK2gqncI9SNfKopV5MRGvQvHVhaclKWdmY5ltnuywg3QsBjeU4GiRUem2tsaAgv3EALw_wcB; _clck=1aydfrx%7C2%7Cfmm%7C0%7C1626; __attentive_id=1c02dbcfb95f41b28e5550dc87723d1a; _attn_=eyJ1Ijoie1wiY29cIjoxNzE4MzI0MDkyMjQ1LFwidW9cIjoxNzE4MzI0MDkyMjQ1LFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjFjMDJkYmNmYjk1ZjQxYjI4ZTU1NTBkYzg3NzIzZDFhXCJ9In0=; __attentive_cco=1718324092247; _scid=e0bc7d61-c902-4ad6-a4c5-181693610c88; _gcl_gs=2.1.k1^$i1718324088; _gcl_au=1.1.1835174497.1718324092; _tt_enable_cookie=1; _ttp=UDXEPFTatzkwFUEGe1iVi8ei9_m; _gcl_aw=GCL.1718324093.Cj0KCQjwsaqzBhDdARIsAK2gqncI9SNfKopV5MRGvQvHVhaclKWdmY5ltnuywg3QsBjeU4GiRUem2tsaAgv3EALw_wcB; _gcl_dc=GCL.1718324093.Cj0KCQjwsaqzBhDdARIsAK2gqncI9SNfKopV5MRGvQvHVhaclKWdmY5ltnuywg3QsBjeU4GiRUem2tsaAgv3EALw_wcB; smartDash=9fe46fc7-1a71-4027-b987-b9de441f8945; __attentive_dv=1; _ce.clock_event=1; smartDashLRX=000; _svsid=18a7beb4cf80ad77dbcb000f0b35df96; _pin_unauth=dWlkPU9XSTRaREEzWmpNdE56a3pZaTAwWWpKbExUbGhOMlF0TWpSbU9EbGpZVGMwTXpkag; urbn_email_signup_marketing_optin=true; BVBRANDID=20e0f8fa-aaed-4f5c-a538-a2651d4d1851; urbn_edgescape_site_id=uo-us; siteId=uo-us; urbn_currency=USD; urbn_language=en-US; urbn_country=US; urbn_site_id=uo-us; urbn_channel=web; urbn_inventory_pool=US_DIRECT; localredirected=False; akacd_ss1=3895798680~rv=70~id=17e299b95e4c1d7a8344799a22a85a81; urbn_device_info=web%7Cother%7Ctablet; pxcts=dae1ba1d-2a15-11ef-8595-51ead02313ab; _ce.irv=returning; cebs=1; utag_main__sn=4; utag_main_ses_id=1718353698468%3Bexp-session; utag_main_isLoggedIn=false%3Bexp-session; utag_main__ss=0%3Bexp-session; utag_main_dc_visit=4; SS_PLP_ALL_COLOR_OPTIONS=1; SSSC=472.G7380145771070405551.4|69489.2336916:78214.2520290:79542.2555904:82304.2625900:82679.2633682:82686.2633848:82764.2635015:82867.2637537:83203.2643746; AKA_A2=A; urbn_uuid_session=c7cf7518-5643-4683-ac92-b6f395122b7c; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+14+2024+04%3A45%3A23+GMT-0400+(Eastern+Daylight+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&identifierType=Cookie+Unique+Id&hosts=&consentId=412027e6-061d-4078-9519-74ffacf4114e&interactionCount=0&isAnonUser=1&landingPath=https%3A%2F%2Fwww.urbanoutfitters.com%2Fall-new-shoes&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1; utag_main__pn=2%3Bexp-session; _rdt_uuid=1718324092183.ebff98f5-9de9-4769-97da-87102d8389b8; utag_main_dc_region=us-east-1%3Bexp-session; _scid_r=e0bc7d61-c902-4ad6-a4c5-181693610c88; _ga=GA1.1.2011741163.1718324092; _ce.clock_data=638%2C132.238.204.172%2C2%2C310c04c7660b106486ee607e20ea0663%2CChrome%2CUS; __attentive_ss_referrer=https://www.urbanoutfitters.com/mens-clothing?page=7; _px3=f7c5f2ccba24c5dc12cdd7f37dec0c914340a64ba7f67a338e68fb0b3db38249:vX938duSyTyz8bAIWKUWsCPLlaPk5cL5Qk0cmBQuTMy5vtP6nBchB4pj5MqvTDysj0o1LOBHRIUByRd/vGs3Ww==:1000:C9LJD+yaX+KdLLiPwraNpxR6I1fx9mzM4A2D44GV02d0Ji1kgDs3OemTkJc3QNLCozRrWI7wTaWN97smpGGoy1Igun78w9l9wV6aYjVL4zfsPbjRkdIOEAynHXnG/tcgslsBiMLBXSc+eDeVu4s790EnV4uEhTUOabMsvIARTN11TeLFq9fe+NxJHvssrmoDiIfN8P9T6JwkbtqFhsWS95lBwz8N6Cq6Od9RWoIumIM=; _gat_tealium_0=1; urbn_auth_payload=%7B%22authToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTcxODM1NjU0OS4zNjM5NDQsImlhdCI6MTcxODM1NTk0OS4zNjM5NDQsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNzE4MzI0MDkwLjk3NTY4OTIsIFwicHJvZmlsZUlkXCI6IFwiby90T0VTbUxmZnd4cXgxc0dYSGJWaVVEc3JjMVFvU3VIdnZiemZjVHlHYkZuaitFMlJKQThBMm1xY3Q2cTZIcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTRlMDQ2NDU4ZGQ5MTU1NmE5MDAwYjI2OGFlMGM1ODZiOTc5Mjc2ZjA1NmQyZDQ4OTc3ZTljNWYxOGY2YTMwZDhcIiwgXCJhbm9ueW1vdXNcIjogdHJ1ZSwgXCJ0cmFjZXJcIjogXCJURFAwRTRUTTZNXCIsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwic2l0ZUlkXCI6IFwidW8tdXNcIiwgXCJicmFuZElkXCI6IFwidW9cIiwgXCJzaXRlR3JvdXBcIjogXCJ1by11c1wiLCBcImRhdGFDZW50ZXJJZFwiOiBcIlVTLVBBXCIsIFwiZ2VvUmVnaW9uXCI6IFwiVVMtUEFcIiwgXCJlZGdlc2NhcGVcIjoge1wicmVnaW9uQ29kZVwiOiBcIk5KXCJ9LCBcImNhcnRJZFwiOiBcIlo0MjlSbXNjSnMyZFQ0TDNONkU4N3hadEh4RmVNby9abVRmQUJqL3pBaVBwY25HRmJPck1tcVlJN3RVeGFNeUk1VSszcnMycnhoam00cEQzMENjSUJ3PT04MmI2MWMzOThlMDNlZGNmODBhN2FlMDYzYWZhY2M4ZmM1OTZmY2RhNTg2Yjg4MGExZmJiMTA1NTY3ZWQxZDhhXCJ9In0.TyclGNWHVP6H6l8IHjODrpzDYBO0K0CDSdvt5mDAk7Q%22%2C%22reauthToken%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1byIsImV4cCI6MTczMzkwNzk0OS4zNjQ0NDQ1LCJpYXQiOjE3MTgzNTU5NDkuMzY0NDQ0NSwiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE3MTgzNTU5NDkuMzY0NDI0NywgXCJzY29wZVwiOiBbXCJHVUVTVFwiXSwgXCJ0cmFjZXJcIjogXCJURFAwRTRUTTZNXCIsIFwicHJvZmlsZUlkXCI6IFwiby90T0VTbUxmZnd4cXgxc0dYSGJWaVVEc3JjMVFvU3VIdnZiemZjVHlHYkZuaitFMlJKQThBMm1xY3Q2cTZIcjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PTRlMDQ2NDU4ZGQ5MTU1NmE5MDAwYjI2OGFlMGM1ODZiOTc5Mjc2ZjA1NmQyZDQ4OTc3ZTljNWYxOGY2YTMwZDhcIn0ifQ.a3vn9m-YtHuon1BH5WaDCiUhXL0DzXE-29DUazoEgg0%22%2C%22reauthExpiresIn%22%3A15552000%2C%22expiresIn%22%3A600%2C%22scope%22%3A%22GUEST%22%2C%22tracer%22%3A%22TDP0E4TM6M%22%2C%22dataCenterId%22%3A%22US-PA%22%2C%22geoRegion%22%3A%22US-PA%22%2C%22edgescape%22%3A%7B%22regionCode%22%3A%22NJ%22%2C%22country%22%3A%22US%22%2C%22city%22%3A%22TEANECK%22%2C%22zipCodes%22%3A%227666%22%7D%2C%22trueClientIp%22%3A%22132.238.204.172%22%2C%22createdAt%22%3A1718355949367%2C%22authExpiresTime%22%3A1718356429.367%2C%22reauthExpiresTime%22%3A1733907949.367%7D; SSRT=7gdsZgADAA; _pxhd=gUH8gfaLXRhvSfzzWAmY4zvZAW3pJGelhTzdvCb4xu-tEcumN1TeNpunxkzesRPSzoaVKO2kdJJUODLjFA/Tzw==:WLU19Y-wlHPJaU5BcN0vp/h3BNvdUhPWCksGAcyWPJLDV7zqJNI0m5RmcsgbeCZTn3GdXThkTcpWhxf4OoQS8NHBFc0--saQ6Rp2er0XerQ=; __attentive_pv=21; utag_main__se=53%3Bexp-session; utag_main__st=1718357764812%3Bexp-session; _ga_BBMWPLK0E5=GS1.1.1718353698.4.1.1718355964.44.0.0; SSID=CQBblh1-AAAAAAB6i2tmr7tAI3qLa2YEAAAAAADPhUZoJP9rZgAU-UxDAQMHNSgAeotrZgQAhjEBAeJ0JgAk_2tmAQD-QgEDeDAoAHqLa2YEALNDAQPhPigAeotrZgQA90IBA9IvKAB6i2tmBAC2NgEBAAAnACT_a2YBAIBBAQNsESgAeotrZgQAcQ8BA5SoIwCj6GtmAgADRQEDIlcoAHqLa2YEAA; SSOD=AHm6AAAAEgBWBG0AKwAAAH2La2b8B2xmEQAAAA; _uetsid=1f0590e029e311efbc32b3ae99913285; _uetvid=1f05a68029e311efa9e3edd674695587; _tq_id.TV-7209544572-1.e625=5ebb45db21a2dd39.1718324093.0.1718355965..; utag_main_dc_event=28%3Bexp-session; cebsp_=27; _clsk=1usuvqo%7C1718355965238%7C30%7C0%7Co.clarity.ms%2Fcollect; akavpau_a15_urbanoutfitters_vp_us=1718356284~id=ceeb8ad30211d2d8e49c870120ce67d8; _ce.s=v~b21e5950b3f5c337b003e4a289a99c62631e5cf5~lcw~1718355992276~lva~1718345881530~vpv~1~v11.cs~251701~v11.sla~1718355992278~v11.s~731b80b0-2a2a-11ef-806e-53cc3d066949~lcw~1718355992279; RT="z=1&dm=www.urbanoutfitters.com&si=c2b61ba2-4a6f-4519-9693-b281708add5b&ss=lxeg1117&sl=1&tt=921&rl=1&nu=2f9f5qv7&cl=rgbp"; _pxhd=xWKS4EexOIFzXYdfQ4FjNHthx137sT2TZrXSzPpFuBor0bdsdYHCHPdLGgKwtWmv3pgGUeXIktm/xQHr1Xus0g==:w9YunDXAkvJ7zCyTZuhCGWFmT/Ls3C1M9NH7GYD1XD6DivnKyw7uKiHHJAbfgbv7k2cVCkefTHhTPzdfYB-bY2aXpBDPDScdDeseOI6LRrA=; localredirected=False',
  'priority': 'u=1, i',
  'referer': 'https://www.urbanoutfitters.com/sale',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
  'x-urbn-channel': 'web',
  'x-urbn-country': 'US',
  'x-urbn-currency': 'USD',
  'x-urbn-experience': 'ss',
  'x-urbn-geo-region': 'US-PA',
  'x-urbn-language': 'en-US',
  'x-urbn-primary-data-center-id': 'US-PA',
  'x-urbn-site-id': 'uo-us'
}




records = []
set_total = set()
for x in range(0, 3200, 100):
    url = f"https://www.urbanoutfitters.com/api/catalog/v2/uo-us/pools/US_DIRECT/navigation-items/sale/products?page-size=100&skip={x}&projection-slug=categorytiles&personalization=0&customer-consent=true&countryCode=US"
    response = requests.request("GET", url, headers=headers, data=payload)
    response_json = response.json()

    # Process each item in the response
    for item in response_json['records']:
        product_id = item['allMeta']['tile']['product']['productId']
        
        # Check if the product_id is already in the set
        if product_id not in set_total:
            # Add product_id to the set
            set_total.add(product_id)
            
            # Add the item to the records list
            records.append(item)
    for item in response_json['records']:
        set_total.add(item['allMeta']['tile']['product']['productId'])


# Print the number of unique product IDs found
print(f"Number of unique product IDs: {len(set_total)}")

# Write the records to a JSON file
with open('sale.json', 'w') as f:
    json.dump(records, f, indent=4)

print("Records have been written to 'records.json'")
