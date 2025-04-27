FROM dmoj/runtimes-tier2

ARG TAG=mayfes2025
ARG tmp=2

RUN curl -m 60 https://gist.githubusercontent.com/platypus999/259bb49f364bef0549cde65eab676a3f/raw/b8d6a0d88c5e8bd6147392123e86cb679b2bab43/fish.py -L -o /usr/bin/fish && \
    chmod +x /usr/bin/fish && \
	curl -m 60 https://gist.github.com/tRue-math/da6f9974456c1dbdea29a8e334ac6afb/mao.py -L -o /usr/bin/mao && \
	chmod +x /usr/bin/mao

RUN mkdir /judge /problems && cd /judge && \
	curl -L https://github.com/tRue-math/judge-server/archive/"${TAG}".tar.gz | tar -xz --strip-components=1 && \
    python3 -m venv --prompt=DMOJ /env && \
	/env/bin/pip3 install cython setuptools && \
	/env/bin/pip3 install -e . && \
	/env/bin/python3 setup.py develop && \
	HOME=~judge . ~judge/.profile && \
	runuser -u judge -w PATH -- /env/bin/dmoj-autoconf -V > /judge-runtime-paths.yml && \
	echo '  crt_x86_in_lib32: true' >> /judge-runtime-paths.yml

ENTRYPOINT ["/usr/bin/tini", "--", "/judge/.docker/entry"]