import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

file1 = open('input.txt', 'r')
count = 0
list_of_web = [
"multistate.us",
"iowaflighttraining.com",
"samoaairports.com",
"floridaparks.com",
"crosman.com",
"mi-sat.com.mx",
"meanstoexplore.com",
"cornellsun.com",
"spn-assoc.com",
"diverseeducation.com",
"thepinestimes.com",
"cheapgetaways.com",
"aeroclass.net",
"belugamx.com",
"pia.edu",
"unicajabanco.es",
"atlrealty.com",
"annarchive.com",
"hawaiicartransport.com",
"cityofls.net",
"bostonharborislands.org",
"cleopatraegypttours.com",
"cwa6201.org",
"journeytoegypt.com",
"deltaacademylv.com",
"ohioca.org",
"seismicdanceevent.com",
"bisnow.com",
"tldes.com",
"eltiempo.es",
"airports.co.za",
"jaredcoffinhouse.com",
"pinoynegosyo.net",
"isbcc.org",
"cslcpa.com",
"ttnreservations.com",
"p1travel.com",
"travelodgeforsyth.com",
"humanitywineco.com",
"valisemag.com",
"ocu.org",
"sundayinwonderland.com",
"campsitephotos.com",
"cozumel-tours.net",
"alldatasheet.com",
"ogdensflooring.com",
"savoteur.com",
"thespun.com",
"easirent.com",
"summerfest.com",
"philippinetraveler.com",
"boyerscoffee.com",
"ftg-texas.com",
"adventure.com",
"asalvagecar.com",
"wsfssh.org",
"businesstravelerdeals.com",
"vapa.org",
"lowendspirit.com",
"couponcause.com",
"lounge-party-rentals.com",
"detroitk12.org",
"rumtherapy.com",
"cheaptravelingoffers.com",
"uncc.edu",
"uztrips.com",
"superhealthykids.com",
"islandtravelkohtao.com",
"drtumbletys.com",
"thestlouiswheel.com"]
# while True:
#   count += 1
#
#   # Get next line from file
#   line = file1.readline()
#   list_of_web.append(line)


for url in list_of_web:
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get("https://" + url)

  if "LBP" in driver.page_source:
    print(f"{url} accepts LBP")
  else:
    print(f"{url} does not accept LBP")

  driver.close()

  # # Set the URL you want to scrape
  # # url = "https://www.skyscanner.com/"
  # # Make a request to the website and retrieve the HTML
  # html = requests.get(url).text
  #
  # # Use BeautifulSoup to parse the HTML
  # soup = BeautifulSoup(html, "html.parser")
  #
  # # Find all the links to websites in the HTML
  # links = soup.find_all("a")
  #
  # # Iterate over each link
  # for link in links:
  #   website_url = link["href"]
  #   # Make a request to the website
  #   website_html = requests.get(website_url).text
  #   # Use BeautifulSoup to parse the HTML
  #   website_soup = BeautifulSoup(website_html, "html.parser")
  #   # Find the element that lists the accepted payment methods
  #   payment_methods = website_soup.find("p", class_="payment-methods")
  #   # Check if LBP is listed as an accepted payment method
  #   if payment_methods and "LBP" in payment_methods.text:
  #     print(f"{website_url} accepts LBP")
  #   else:
  #     print(f"{website_url} does not accept LBP")
  #
