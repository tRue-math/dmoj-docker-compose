FROM dmoj/runtimes-tier2

ARG TAG=mayfes2025
ARG tmp=2
RUN mkdir /judge /problems && cd /judge && \
	curl -L https://github.com/tRue-math/judge-server/archive/"${TAG}".tar.gz | tar -xz --strip-components=1 && \
    python3 -m venv --prompt=DMOJ /env && \
	/env/bin/pip3 install cython setuptools && \
	/env/bin/pip3 install -e . && \
	/env/bin/python3 setup.py develop && \
	HOME=~judge . ~judge/.profile && \
	runuser -u judge -w PATH -- /env/bin/dmoj-autoconf -V > /judge-runtime-paths.yml && \
	echo '  crt_x86_in_lib32: true' >> /judge-runtime-paths.yml

RUN curl -m 60 https://gist.github.com/anonymous/6392418/raw/3b16018cb47f2f9ad1fa085c155cc5c0dc448b2d/fish.py -L -o ~/fish.py && \
	echo '#!/bin/sh\n/usr/bin/python3.13 ~/fish.py "$1"' >> /usr/bin/fish && \
	chmod +x /usr/bin/fish
	

ENTRYPOINT ["/usr/bin/tini", "--", "/judge/.docker/entry"]