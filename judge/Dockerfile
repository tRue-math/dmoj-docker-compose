FROM dmoj/runtimes-tier2

ARG TAG=mayfes2025
ARG TIMEOUT=60

RUN apt-get update && \
    apt-get install -y git libtiff-dev libgdiplus erlang elixir
RUN	curl -m ${TIMEOUT} https://gist.githubusercontent.com/platypus999/259bb49f364bef0549cde65eab676a3f/raw/b8d6a0d88c5e8bd6147392123e86cb679b2bab43/fish.py -L -o /usr/bin/fish && \
    chmod +x /usr/bin/fish && \
	curl -m ${TIMEOUT} https://gist.githubusercontent.com/tRue-math/da6f9974456c1dbdea29a8e334ac6afb/raw/7533756e0c4622b809c4adbf4be5cdbb49579247/mao.py -L -o /usr/bin/mao && \
	chmod +x /usr/bin/mao && \
	runuser -u judge curl -m ${TIMEOUT} https://sh.rustup.rs -sSf | sh && \
	curl -m ${TIMEOUT} https://gist.githubusercontent.com/tRue-math/0265103969895f168612096eb783f7c0/raw/5112559a96433503960c160ffe1f295d6566e794/starry.rb -L -o /usr/bin/starry && \
	chmod +x /usr/bin/starry && \
	git clone --depth 1 https://github.com/dnek/mines-esolang.git /opt/mines && \
	echo '#!/bin/sh\nexec /usr/bin/python3 /opt/mines/mines/mines.py "$@"' > /usr/bin/mines && \
	chmod +x /usr/bin/mines && \
	curl -m ${TIMEOUT} https://gist.githubusercontent.com/tRue-math/95c2937888f106def8a96e37f76a73b9/raw/61c9876c1121886eaa7bff15fed60b73268018af/ferNANDo.py -L -o /usr/bin/fernando && \
	chmod +x /usr/bin/fernando && \
	cd /tmp && \
	git clone --depth 1 https://github.com/aheui/caheui.git && \
	cd caheui && make && mv aheui /usr/bin/aheui && \
	cd /tmp && \
    curl https://rdr.utopiat.net/files/mono//produire-mono-1.9.1182.tar.gz -LO && \
    mkdir -p /usr/lib/mono/produire && \
    tar xf produire-mono-1.9.1182.tar.gz -C /usr/lib/mono/produire && \
	echo '#!/bin/sh\nexec /usr/bin/mono /usr/lib/mono/produire/produire-mono/pconsole.exe "$@"' > /usr/bin/produire && \
	chmod +x /usr/bin/produire && \
	cd /opt && \
	git clone --depth 1 https://github.com/Adriandmen/05AB1E.git && \
	cd 05AB1E && (yes | PATH=/usr/bin:$PATH mix local.hex) && \
    PATH=/usr/bin:$PATH mix deps.get && \
	mix deps.update hackney && \
    (yes | PATH=/usr/bin:$PATH MIX_ENV=prod mix escript.build) && \
	echo '#!/bin/sh\nexec /usr/bin/escript /opt/05AB1E/osabie "$@"'>/usr/bin/05ab1e && \
	chmod +x /usr/bin/05ab1e && \
	cd && \
    rm -rf /var/cache/apk/* /tmp/*

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