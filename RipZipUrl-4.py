import requests
from lxml.html import etree

"""
 This downloader downloads all .zip files behind links in a catalog it is pointed to
 This is version 4 of the brute downloader. A haphazard mishmash of hardcoded parts that work.
 Made by kriminaaliSM
"""

# Enter your downloads page URL
archive_url = "https://YOURURL/TO/Downloads-link-list"
response = requests.get(archive_url)


# below is very important- and useful

# filter the links to only .zip-files , reference html <a>-tag href
def link_extraction():
    doc_tree = etree.HTML(response.content)
    hrefs = doc_tree.xpath('//a/@href')
    zip_links = [ref for ref in hrefs if ref.endswith('.zip')]
    return zip_links


# downloader proper
def download_zip_archives(zip_links):
    for link in zip_links:

        # go through zip_links one by one

        # obtain filename by splitting url and getting last string part
        file_name = link.split('/')[-1]

        print("Downloading file:%s" % file_name)

        # create response object brute-force append https-address to front
        # real dumb, but it works hardcoded. Too afraid to change link into archive_url
        r = requests.get(archive_url + link, stream=True)

        # download started
        # with open keeps things clean and closes files after use
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All zips downloaded!")
    return


if __name__ == "__main__":
    # getting all archive links
    zip_links = link_extraction()

    # download all archives
    download_zip_archives(zip_links)
