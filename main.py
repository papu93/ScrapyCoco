from ScrapyCocoProviders.crawler_run import ScrapyCocoProviders

product = 'llantas'
celulares = ScrapyCocoProviders(product)
celulares.runMercadoLibre()