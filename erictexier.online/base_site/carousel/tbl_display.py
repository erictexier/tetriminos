from collections import namedtuple
from pprint import pprint

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

class tumb_post(namedtuple('Tbl',
    'blog_name blog tags date pic_url mult_url caption image_permalink')):
    __slots__ = ()


class TblDisplay(dict):
    """ helper to display template """
    _tkey = [
            'blog_name',
            'blog',
            'caption',
            'tags',
            'date']

    _fkey = _tkey + [
            'pic_url',
            'mult_url'
            ]

    def __init__(self):
        self['caption'] = "untitled"
        self['pic_url'] = ""
        self['image_permalink'] = ""
        self['mult_url'] = list()

    def from_data_tumblr(self, data_tumblr):
        for k in TblDisplay._tkey:
            if k in data_tumblr:
                if k != 'caption':
                    self[k] = data_tumblr[k]
                elif data_tumblr[k] != '':
                    self[k] = cleanhtml(data_tumblr[k])

        if 'photos' in data_tumblr and len(data_tumblr['photos']) > 0:
            #if ('caption' in data_tumblr['photos'] and 
            #    data_tumblr['photos'][0]['caption'] != ""):
            #    print("f"* 100)
            # self['caption'] = data_tumblr['photos'][0]['caption']
            #pprint (data_tumblr)
            self['pic_url'] = data_tumblr['photos'][0]['original_size']
            #print(data_tumblr['photos'][0]['original_size'])
            #'width': 1280, 'height': 853

        if 'photos' in data_tumblr:
            for p in data_tumblr['photos'][1:]:
                self['mult_url'].append(p['original_size'])

        if 'image_permalink' in data_tumblr:
            self['image_permalink'] = data_tumblr['image_permalink'].replace('image','post')
        
        if 'date' in self:
            self['date'] = self['date'].split(" ")[0]
        
        self['tags'] = [x.strip() for x in self['tags'] if x.strip() != ""]
    
    def is_valid(self):
        if self['pic_url'] == "":
            return False
        return True

    def from_dict_file(self, dict_from_file):
        for k in TblDisplay._fkey:
            self[k] = dict_from_file[k]


    @staticmethod
    def filter_valid(alist):
        return [x for x in alist if x.is_valid()]
