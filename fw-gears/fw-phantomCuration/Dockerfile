FROM flywheel/fw-gear-ants-base:2.3.5

ENV FLYWHEEL='/flywheel/v0'
RUN mkdir -p ${FLYWHEEL}
WORKDIR ${FLYWHEEL}

RUN pip install "poetry==1.2.0"

COPY pyproject.toml poetry.lock $FLYWHEEL/
RUN poetry install --only main 

RUN pip install flywheel-gear-toolkit 

COPY run.py manifest.json README.md $FLYWHEEL/
COPY app $FLYWHEEL/app
RUN poetry install --only main

RUN chmod a+x $FLYWHEEL/run.py
ENTRYPOINT ["poetry","run","python","/flywheel/v0/run.py"]


