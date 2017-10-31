from ScrapyCocoProviders.crawler_run import ScrapyCocoProviders
import json

product = 'llantas'
celulares = ScrapyCocoProviders(product)
celulares.run_mercado_libre()
print(celulares.get_results())
