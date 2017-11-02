from ScrapyCocoProviders.crawler_run import ScrapyCocoProviders

search = ScrapyCocoProviders('celulares', 5)
print(search.run_mercado_libre())
