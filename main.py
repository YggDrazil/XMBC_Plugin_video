# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {'Lesben': [{'name': 'Gym only for Three Lesbians',
                       'thumb': 'http://s21.bigcdn.cc/pub/cid/58eb0df82513b/main.jpg',
                       'video': 'http://s21.bigcdn.cc/pub/cid/58eb0e14d71d8/720.mp4',
                       'genre': 'Lesben'},
                      {'name': 'Fantasy about Mom and her Stepdaughter ',
                       'thumb': 'http://s7.bigcdn.cc/pub/cid/58eb07f6581b0/main.jpg',
                       'video': 'http://s7.bigcdn.cc/pub/cid/58eb080d59063/720.mp4',
                       'genre': 'Lesben'},
                     {'name': 'Little Caprice and Chrissy Fox',
                       'thumb': 'http://s11.bigcdn.cc/pub/cid/58eb1d4fd3256/main.jpg',
                       'video': 'http://s11.bigcdn.cc/pub/cid/58eb1da142cf9/720.mp4',
                       'genre': 'Lesben'},
                      {'name': 'From Russia with Love by Maria',
                       'thumb': 'http://s15.bigcdn.cc/pub/cid/58eaffb4a8462/main.jpg',
                       'video': 'http://s15.bigcdn.cc/pub/cid/58eaffc743b55/720.mp4',
                       'genre': 'Lesben'}
                      ],
            'Teenie': [{'name': 'Grosser Schwanz in kleiner Muschi',
                      'thumb': 'http://s12.bigcdn.cc/pub/cid/58eb0b5a9bbe7/main.jpg',
                      'video': 'http://s13.bigcdn.cc/pub/cid/58eb08554b291/720.mp4',
                      'genre': 'Teenie'},
                     {'name': 'While Student Girls are playing Games...',
                      'thumb': 'http://s14.bigcdn.cc/pub/cid/58eb0bb227db7/main.jpg',
                      'video': 'http://s19.bigcdn.cc/pub/cid/58eb0c7b0b695/720.mp4',
                      'genre': 'Teenie'},
                       {'name': 'Sexy Teacher seduced a Young Guy',
                      'thumb': 'http://s11.bigcdn.cc/pub/cid/58eb15ac2ab6c/main.jpg',
                      'video': 'http://s11.bigcdn.cc/pub/cid/58eb15e718465/720.mp4',
                      'genre': 'Teenie'},
                       {'name': 'Beautiful Foursome ',
                      'thumb': 'http://s17.bigcdn.cc/pub/cid/58eb17493530a/main.jpg',
                      'video': 'http://s17.bigcdn.cc/pub/cid/58eb175c55ee9/720.mp4',
                      'genre': 'Teenie'},
                     {'name': 'Zwei Junge Mädels beim Klauen erwischt',
                      'thumb': 'http://s20.bigcdn.cc/pub/cid/58eb0db1a8a15/main.jpg',
                      'video': 'http://s20.bigcdn.cc/pub/cid/58eb0d6f2dca3/720.mp4',
                      'genre': 'Teenie'}
                     ],
            'Ebony': [{'name': 'My Strict Teachers',
                      'thumb': 'http://s17.bigcdn.cc/pub/cid/58eb07b653836/main.jpg',
                      'video': 'http://s17.bigcdn.cc/pub/cid/58eb07b653836/720.mp4',
                      'genre': 'Ebony'},
                     {'name': 'Exactly what Black Mom Want to Do',
                      'thumb': 'http://s1.bigcdn.cc/pub/cid/58eafa40d6055/main.jpg',
                      'video': 'http://s18.bigcdn.cc/pub/cid/58eb093a1d5f5/720.mp4',
                      'genre': 'Ebony'},
                      {'name': 'Russian Boy fucks Sweet Black Girl',
                      'thumb': 'http://s7.bigcdn.cc/pub/cid/58eb04b48ce8b/main.jpg',
                      'video': 'http://s7.bigcdn.cc/pub/cid/58eb04d517b5a/720.mp4',
                      'genre': 'Ebony'},
                      {'name': 'A Resourceful Stepdaddy',
                      'thumb': 'http://s19.bigcdn.cc/pub/cid/58eb0b541edd1/main.jpg',
                      'video': 'http://s19.bigcdn.cc/pub/cid/58eb0b6941f96/720.mp4',
                      'genre': 'Ebony'},
                     {'name': 'Black Girls getting Creampie',
                      'thumb': 'http://s20.bigcdn.cc/pub/cid/58eb0a4b356d7/main.jpg',
                      'video': 'http://s20.bigcdn.cc/pub/cid/58eb0a5f68ccf/720.mp4',
                      'genre': 'Ebony'}
                     ],
          'Threesome': [{'name': 'She get more Fun with One more Cock',
                       'thumb': 'http://s15.bigcdn.cc/pub/cid/58eb132056ef1/main.jpg',
                       'video': 'http://s15.bigcdn.cc/pub/cid/58eb13b02b669/720.mp4',
                       'genre': 'Threesome'},
                      {'name': 'Very Interracial Lesbian Threesome',
                       'thumb': 'http://s10.bigcdn.cc/pub/cid/58eb21b7478a1/main.jpg',
                       'video': 'http://s10.bigcdn.cc/pub/cid/58eb21f498638/720.mp4',
                       'genre': 'Threesome'},
                     {'name': 'stepsister gone crazy',
                       'thumb': 'http://s9.bigcdn.cc/pub/cid/58eb23ed06ad4/main.jpg',
                       'video': 'http://s9.bigcdn.cc/pub/cid/58eb24156a862/720.mp4',
                       'genre': 'Threesome'},
                      {'name': 'Paula Shy between Two Cocks',
                       'thumb': 'http://s7.bigcdn.cc/pub/cid/58eb1df29356b/main.jpg',
                       'video': 'http://s7.bigcdn.cc/pub/cid/58eb1dfbb62d1/720.mp4',
                       'genre': 'Threesome'}
                      ],
         'Russian': [{'name': 'Nedda from Russia',
                      'thumb': 'http://s7.bigcdn.cc/pub/cid/58eb134dbc1ee/main.jpg',
                      'video': 'http://s9.bigcdn.cc/pub/cid/58eb1a5d0ce03/720.mp4',
                      'genre': 'Russian'},
                      {'name': 'Relaxation before Fucking',
                      'thumb': 'http://s2.bigcdn.cc/pub/cid/58eb1ce25c2e4/main.jpg',
                      'video': 'http://s18.bigcdn.cc/pub/cid/58eb1c626c9f0/720.mp4',
                      'genre': 'Russian'},
                      {'name': 'Bonus for Good Work',
                      'thumb': 'http://s13.bigcdn.cc/pub/cid/58eb19350ff4f/main.jpg',
                      'video': 'http://s5.bigcdn.cc/pub/cid/58eb1a697533b/720.mp4',
                      'genre': 'Russian'},
                      {'name': 'Naked Surprise',
                      'thumb': 'http://s6.bigcdn.cc/pub/cid/58eb39750d66f/main.jpg',
                      'video': 'http://s4.bigcdn.cc/pub/cid/58eb1d424f587/720.mp4',
                      'genre': 'Russian'},
                     {'name': 'Sicilia and Haley Hill',
                      'thumb': 'http://mirror.mydaddy.cc/pub/cid/58eb248bb988e/main.jpg',
                      'video': 'http://s20.bigcdn.cc/pub/cid/58eb1e5c0c694/720.mp4',
                      'genre': 'Russian'}
                     ]}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.iterkeys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
