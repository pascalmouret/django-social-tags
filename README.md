# django-social-tags
This tool is supposed to make it easier to handle the meta attributes that are often needed for social networks, for example OpenGraph, which is used by Facebook and Google+.

## Supported Networks
* Facebook (OpenGraph)
* Google (OpenGraph)
* Twitter (Cards API)

## Installation
The installation is a bit of a pain in the ass.

1. Install the `django-social-tags` as you would everything else (e.g. `pip install django-social-tags`)
2. add `'social_tags'` to your `INSTALLED_APPS` in your `settings.py`
3. insert `'social_tags.context_processors.social'` into `TEMPLATE_CONTEXT_PROCESSORS`
4. in your base template (it has to be the base template):

    1. add `social_meta` and `sekizai_tags` to your `{% load %}` tag.
    2. add the line 
        `{% with_data 'social_tags' as data %}{% render_meta_tags data %}{% end_with_data %}`
        inside the `<head>` tag.

I realize the last step is still pretty ugly, working on that.

## Usage
The values for the tags are collected on three levels (sorted by priority top to bottom):

1. Template/Request
2. Context
3. Preset defaults

### Defaults
For most attributes there is a setting in the form of `SOCIAL_TAGS_DEFAULT_ATTRIBUTE`.

### Context
To modify some value out of a view, simply modify the `context['social_tags']` dictionary.

### Template
After loading the `social_meta` tag library, you can set attributes via `{% set_tag attribute value %}`

## Custom Networks
You need a network not yet included? No problem, you can easily write your own!

Simply add the file `social_tags_networks` to a package in `INSTALLED_APPS` and add a `Network` object. Since code says it best, here a simple example:

```python

from social_tags.networks import Network, networks, SocialTagsValidationError

class HelloWorld(Network):
	name = 'hello_world'
	template = 'networks/hello_world.html'
	
	def prepare_context(self, context):
		'''
		The context contains all collected data from defaults, context and
		templates.
		Network specific data is stored in context[name].
		'''
		context['description'] = 'I wan\'t my own description!'
		context['hello_world']['text'] = 'Hello World'
		return context
		
	def debug(self, context):
		'''
		This will only be executed if DEBUG = True.
		'''
		if not hasattr(context, 'photo'):
			raise SocialTagsValidationError('A photo is required!')
networks.register(HelloWorld)
```

You will of course also need a template, which could look something like this:

```html
<meta name="helloworld" content="{{ hello_world.text }}" />
```

This is still experimental, so there could still be a lot of changes.