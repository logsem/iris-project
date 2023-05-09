FROM ruby:2.7-slim-bullseye

RUN apt-get update && apt-get install -y \
    build-essential \
    ruby2.7-dev

RUN mkdir /iris-project
COPY Gemfile /iris-project/Gemfile
WORKDIR /iris-project
RUN gem install bundler:2.4.6
RUN bundle install

CMD bundle exec jekyll serve --watch --host 0.0.0.0
