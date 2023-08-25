FROM r-base
COPY . /usr/local/src/myscripts
WORKDIR /usr/local/src/myscripts
RUN R -e "install.packages('microeco')"
CMD [ "Rscript", "work1.R"]
