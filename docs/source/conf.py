# -*- coding: utf-8 -*-

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Cenderavouz'
copyright = u'2018, Cenderavouz'
author = u'Cenderavouz'

release = ''
language = u'id'

exclude_patterns = []
exclude_patterns = ['README.rst', 'venv*', 'env*']
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_theme = 'classic'
html_static_path = ['_static']
html_show_sourcelink = False
html_copy_source = False
html_show_copyright = False

rst_epilog = """
.. |more| image:: /_static/img/ui/ic_more_vert_black_48dp.png
   :width: 1 em
.. |done| image:: /_static/img/ui/ic_done_black_48dp.png
   :width: 1 em
.. |play_| image:: /_static/img/ui/ic_slideshow_black_48dp.png
   :width: 1 em
.. |addc| image:: /_static/img/ui/ic_add_circle_black_48dp.png
   :width: 1 em
.. |edit| image:: /_static/img/ui/ic_mode_edit_black_48dp.png
   :width: 1 em
.. |copy| image:: /_static/img/ui/ic_content_copy_black_48dp.png
   :width: 1 em
.. |del| image:: /_static/img/ui/ic_delete_black_48dp.png
   :width: 1 em
"""

# -- Options for HTMLHelp output ------------------------------------------
htmlhelp_basename = 'Cenderavouz'

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'a4paper',
    'releasename':" ",
}

latex_documents = [
    ('db/templat/stokharian/index', 'stokharian.tex', u'Dokumentasi Templat Stok Harian',
     author, 'manual'),
]

latex_show_urls = 'footnote'
#latex_elements = { 'releasename': ' ' } # --> bermasalah


# -- Options for manual page output ---------------------------------------
man_pages = [
    (master_doc, 'dokumentasiCenderavouz', u'Dokumentasi Cenderavouz',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    (master_doc, 'cenderavouz', u'Cenderavouz',
     author, 'Cenderavouz', 'Cenderavouz.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']













