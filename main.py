from ScrapyCocoProviders.crawler_run import ScrapyCocoProviders
import json

product = 'celulares'
celulares = ScrapyCocoProviders(product, 5)
celulares.run_mercado_libre()
print(celulares.get_results())
