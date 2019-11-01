from .parser_instr import *

if __name__ == '__main__':
    urls_dict = {}
    get_links_from_xlsx(urls_dict)
    get_price_from_isntr_site(urls_dict)