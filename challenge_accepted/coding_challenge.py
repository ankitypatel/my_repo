# -*- coding: utf-8 -*-

import sys
import os
import json
import re

########################################################################
#
#  Name        : Ankit Patel (ankitypatel21@gmail.com)
#  Description : This program is taking data objects from products.txt and listings.txt, and
#                creates data object of product name and suitable listing.
#                Resulted data object is stored in result_file.txt.
#
#
########################################################################

product_list=[]               # list of products.txt objects
retail_list=[]                # list of listings.txt objects
result_dict={}                # result object in result_file.txt
retail_element_list=[]        # list of listings.txt objects respect to product_name
product_element_track=[]      # list of product name ,to keep track of processed products


def create_procuct_listing():
  '''
      This function is traverse retail list and finds suitable listing for perticular product
      and writes result data in "result.txt" in jason format.
  '''
  result_file=open("result_file.txt","wb+");   # open file for writing result data
  result_file.seek(0,0);

  for product_element in product_list:

    if product_element["product_name"] not in product_element_track:  # avoid repetation of same product

      product_element_track.append(product_element["product_name"])
      for retail_element in retail_list:
        # search for suitable listing respect to product manufecturer and model
        if (re.search(product_element['manufacturer'],retail_element["title"],flags=re.I)) and \
           (re.search(product_element["model"]+' ',retail_element["title"],flags=re.I)):

          result_dict["product_name"] = product_element["product_name"]
          retail_element_list.append(retail_element)
          result_dict["listings"] = retail_element_list

      if result_dict:
        json.dump(result_dict,result_file)  #write result data to result_file.txt
        result_file.write('\n')
        result_dict.clear()
      del retail_element_list[:]

  if os.stat("result_file.txt").st_size:
    return True;
  else:
    return False;


if __name__=="__main__":

  '''main function: open product.txt and listings.txt to read, and convert into list form '''

  try:
    product_file= open("products.txt","r+");
  except:
    print "products.txt not found!";
  try:
    listing_file= open("listings.txt","r+");
  except:
    print "listings.txt not found "

  # add element from product.txt to product_list
  for line in product_file:
    product_list.append(json.loads(line));
  # add element from listings.txt to retail_list
  for line in listing_file:
    retail_list.append(json.loads(line));

  if create_procuct_listing():
    print "\r\tprocess : completed !!\t"
    print "\n****** product list is ready in result_file.txt ****** \n"
  else:
    print "\nfile is empty, something is wrong\n"



