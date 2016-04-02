# -*- coding: utf-8 -*-

import sys
import os
import json
import re

product_list=[]
retail_list=[]
result_dict={}

def create_procuct_listing():
  '''
      This function is traverse retail list and finds suitable listing for perticular product
      and writes result data in "result.txt" in jason format.
  '''
  i=0
  result_file=open("result_file.txt","w+");   # open file for writing result data
  result_file.seek(0,0);

  for product_element in product_list:

    for retail_element in retail_list:
      # search for suitable listing respect to product manufecturer and model

      if (re.search(product_element['manufacturer'],retail_element["title"],flags=re.I)) and \
         (re.search(product_element["model"]+' ',retail_element["title"],flags=re.I)):

        result_dict["product_name"]=product_element["product_name"]
        result_dict["listings"]=retail_element
        json.dump(result_dict,result_file, indent=1)  #write result data to result_file.txt

  if os.stat("result_file.txt").st_size:
    return True;
  else:
    return False;


if __name__=="__main__":

  '''main function: open product.txt and listings.txt to read, and convert into list form '''

  try:
    product_file= open("products.txt","r+");
  except:
    print "product.txt not found!";
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



