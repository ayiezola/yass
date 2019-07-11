# YASS - Yet Another Subdomainer Software

[![Build Status](https://travis-ci.org/mrnfrancesco/yass.svg?branch=master)](https://travis-ci.org/mrnfrancesco/yass)
[![Code Climate](https://codeclimate.com/github/mrnfrancesco/yass/badges/gpa.svg)](https://codeclimate.com/github/mrnfrancesco/yass)

YASS is a plugin-powered search engine based subdomainer.
Its goal is to give you a tool to query whatever search engine you like and parse HTML response writing *less than 10 lines of code*.

#### YASS Plugins
YASS comes with some pre-built plugins:

- Aol
- Ask
- Baidu
- Bing
- Google
- StartPage
- WebCrawler
- Yahoo

You can look at them in `yass/plugins.py`.

##### How to write a new YASS plugin

YASS plugins follow just a few rules:

1. All the plugins are stored in `yass/plugins.py` module.

2. Every plugin MUST subclass `yass.models.PluginBase` and define an inner class named `Meta` with the following attributes in it:

    - `search_url` [mandatory],  a string representing the base URL for the search engine
    - `query_param` [default: `'q'`], the parameter used to store the query
    - `include_param` [default: `'site%3A'`], the parameter to use in the search engine to search for a specific domain
    - `exclude_param` [default: `'-site%3A'`], the parameter to use in the search engine to exclude a specific domain from the results
    - `subdomains_selector` [mandatory], the jQuery selector (yes, jQuery) where to find the subdomains from the results page
    - `request_delay` [default: `.250`], the number of seconds to wait after every query before querying again

3. You can use the default plugin behaviour in most cases, but if you need to change it you could override these methods only:

    - `url(self, exclude_subdomain=None)`, it provide the query string based on `Meta` attributes
    - `extract(self, elements)`, it extract an URL string from an `Element` list of objects (look at `PyQuery` to know how it works)
    - `clean(self, urls)`, it remove useless parts from a list of URLs to get the subdomain string only

#### INSTALL

YASS is fully compatible with Python 3.7 and have just two requirements:

- PyQuery >= 1.2.9
- Colorama

To install YASS and its requirements:

    git clone https://github.com/mrnfrancesco/yass.git  # or download and unzip release archive
    cd yass
    ./setup.py install

#### USAGE

    usage: yass [-g] [-d] [-l {debug,info,warning,error,critical}] [-c | -nc] [-h]
                [-u] [-v]
                DOMAIN [SUBDOMAIN [SUBDOMAIN ...]]
    
    positional arguments:
      DOMAIN                the domain to search for
      SUBDOMAIN             the list of subdomains to exclude
    
    Output arguments:
      -g, --grepable        output results in grepable format (default: False)
      -d, --debugging       set output format to a more verbose one, for debugging
                            purpose (default: False)
      -l {debug,info,warning,error,critical}, --level {debug,info,warning,error,critical}
                            set output verbosity (default: info)
      -c, --color           use color in the output (default: True)
      -nc, --no-color       do not use color in the output
    
    Informations:
      -h, --help            show this help and exit
      -u, --usage           show the usage and exit
      -v, --version         show the framework version an exit
