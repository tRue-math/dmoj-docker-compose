FROM dmoj/runtimes-tier2

ARG TAG=komabafes2025
ARG TIMEOUT=60

RUN apt-get update && \
    apt-get install -y git libtiff-dev libgdiplus erlang elixir gcc-12
RUN	runuser -u judge curl -m ${TIMEOUT} https://sh.rustup.rs -sSf | sh && \
	curl -m ${TIMEOUT} https://github.com/dnek/mines-esolang/archive/d5694877a24f6c37a9c84a848febc683baffddc2.zip -L -o /opt/mines.zip && \
	unzip /opt/mines.zip -d /opt/mines && \
	mv /opt/mines/mines-esolang-*/* /opt/mines && \
	rm -rf /opt/mines/mines-esolang-* && \
    curl https://rdr.utopiat.net/files/mono//produire-mono-1.9.1182.tar.gz -LO && \
    mkdir -p /usr/lib/mono/produire && \
    tar xf produire-mono-1.9.1182.tar.gz -C /usr/lib/mono/produire && \
	/usr/bin/pip3 install --break-system-packages getch && \
	cd /opt && \
	git clone --depth 1 https://github.com/Adriandmen/05AB1E.git && \
	cd 05AB1E && (yes | PATH=/usr/bin:$PATH mix local.hex) && \
    PATH=/usr/bin:$PATH mix deps.get && \
	mix deps.update hackney && \
    (yes | PATH=/usr/bin:$PATH MIX_ENV=prod mix escript.build) && \
	cd && \
    rm -rf /var/cache/apk/* /tmp/*

COPY ./scripts /usr/bin/
RUN chmod -R a+rx /usr/bin/

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