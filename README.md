# My personal website

## Main info

This repository hosts the source code for my personal website.

I have enough experience to create interesting websites, but I want my personal web page to be simple and easy to understand. I want it to be straightforward, with text as the main component.

Even though it looks pretty basic, the website has a lot more going on. This repository also hosts the source code for a simple build script that runs on push and renders markdown files into HTML pages.

At the moment, the site is hosted on CloudFlare Pages, but once GitVerse Pages is released, I'm thinking about moving it there.

## Current navigation

- [/](https://mrkrk.me/) - Main page
- [/projects](https://mrkrk.me/projects) - List of projects
- [/gallery](https://mrkrk.me/gallery) - My photos gallery
- [/blog](https://mrkrk.me/blog) - Old blog posts

**NOTE:** After deleting my Telegram channel, I wanted to delete all my blog posts. However, I decided not to delete the publications from this site, so the page is just hidden, but you can still access it. 

## About 404 Page

I didn't want to create a 404 page. I wanted to keep things simple so that all pages would be rendered by the build script. However, CloudFlare Pages forwards to the main page of the site if the page is not found, which interferes with the search results. So I had to create my own 404 page.

**CLOUDFLARE CREATE A DEFAULT 404 PAGE PLEASE**

## About HTML minification

The build script has some issues with indentation and code beautification. I'm too lazy to fix them, so I decided to minify the rendered HTML instead.

I'm using [this excellent tool](https://github.com/wilsonzlin/minify-html) to minify rendered HTML.

## About Linguist settings

Markdown, by default, is not marked in the repository stats in GitHub as a language used in the project. I've set special settings in `.gitattributes` to show it. 

I want to show that most of the work is done by a simple build script, and the content can be edited easily. Even with this simple approach, everything can function fully.

## A little historical note

Previously, I didn't want to simplify the site that much, and there are a lot more pages and material here. You can see the old version [here](https://41ecb9be.arbuzicu.pages.dev/).

P.S. `*.pages.dev` might not work for you. :/
