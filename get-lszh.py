# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:20:09 2020

@author: simon
"""

import requests					# requesting webpages
import json
import optparse

parser = optparse.OptionParser('get-lszh')
parser.add_option('-o', '--outdir',	dest='outdir', help='[optional] output directory')
parser.add_option('-s', '--single-file',	action='store_true', dest='single', help='[optional] save to single file')
parser.add_option('-p', '--spotter-only',	action='store_true', dest='spotter', help='[optional] only save the spotter relevant flights')
(opts, args) = parser.parse_args()

headers = { 'Host': 'dxp-fds.flughafen-zuerich.ch',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'}

def getLSZH(tabletyp, spotter=False):
    requrl = 'https://dxp-fds.flughafen-zuerich.ch/flights'
    # website currently does not require to send the headers
    response = requests.get(requrl, headers=headers)
    
    if(response.status_code != 200):
        print('error: Website returned status code: ' + str(response.status_code))
    
    timetable = []
    if("flightType" in response.text):
        rawtable = json.loads(response.text)
        for flight in rawtable:
            # arrivals
            if('arr' in tabletyp.lower()):
                if('a' in flight['flightType'].lower()):
                    # only count as spotter if isCommercial = false
                    if(spotter == True):
                        if('isCommercial' in flight):
                            if(flight['isCommercial'] == True):
                                timetable.append(flight)
                    else:
                        timetable.append(flight)
            # departures
            else:
                if('d' in flight['flightType'].lower()):
                    # only count as spotter if isCommercial = false
                    if(spotter == True):
                        if('isCommercial' in flight):
                            if(flight['isCommercial'] == True):
                                timetable.append(flight)
                    else:
                        timetable.append(flight)  
    return timetable

def writeJsonFile(filename, data):
    with open(str(filename), 'w') as outfile:
        json.dump(data, outfile)

#%%
def main():
    try:
        outdir = './lszh'
        if(opts.outdir is not None):
            outdir = opts.outdir
            
        # opts.spotter = True
        
        fileapp = '.json'
        if(opts.spotter is True):
            fileapp = '.spotter.json'
 
        table = {}
        table['data'] = []
        if(opts.single is not None):
            table['data'] = getLSZH('arr', opts.spotter)
            table['data'] = table['data'] + getLSZH('dep')
            # sort by arrital time
            table['data'] = sorted(table['data'], key=lambda k: k['scheduledTime']) 
            writeJsonFile(outdir + '/timetable' + fileapp, table)
        else:
            table['data'] = getLSZH('arr', opts.spotter)
            writeJsonFile(outdir + '/arrivals.timetable' + fileapp, table)
            table['data'] = getLSZH('dep', opts.spotter)
            writeJsonFile(outdir + '/departures.timetable' + fileapp, table)
        
    except KeyboardInterrupt:
        print('')
        exit(0)

if __name__ == '__main__':
	main()
    
    
