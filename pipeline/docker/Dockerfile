# We need to make a central version of the parent
FROM joezuntz/desc-pipe-base:1.0

# Install dependencies
RUN apt-get install -y libffi-dev && apt-get clean

RUN pip3 install TreeCorr twopoint
RUN apt-get install -y git && apt-get clean

# Add the github repo code.  If you need to change the actual install process that's no problem.
# We don't install things centrally to make debugging easier.
RUN cd /opt \
    && git clone https://github.com/joezuntz/ngmix_2pt

ENV PYTHONPATH="/opt/ngmix_2pt/python:${PYTHONPATH}"
ENV PATH="/opt/ngmix_2pt/bin.src:${PATH}"

USER vagrant
