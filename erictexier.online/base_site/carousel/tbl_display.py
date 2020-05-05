
class TblDisplay(dict):
    """ helper to display template """
    _tkey = [
            'blog_name',
            'blog',
            # 'photos',
            'tags',
            'date']

    def __init__(self, data_tumblr):
        for k in TblDisplay._tkey:
            if k in data_tumblr:
                self[k] = data_tumblr[k]
        self['caption'] = "No Caption"
        self['pic_url'] = ""
        self['image_permalink'] = ""
        self['mult_url'] = list()
        if len(data_tumblr['photos']) > 0:
            if 'photos' in data_tumblr and 'caption' in data_tumblr['photos'][0]:
                self['caption'] = data_tumblr['photos'][0]['caption']
            self['pic_url'] = data_tumblr['photos'][0]['original_size']['url']
        for p in data_tumblr['photos'][1:]:
            self['mult_url'].append(p['original_size']['url'])

        if 'image_permalink' in data_tumblr:
            self['image_permalink'] = data_tumblr['image_permalink'].replace('image','post')
        
        if 'date' in self:
            self['date'] = self['date'].split(" ")[0]