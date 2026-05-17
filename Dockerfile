FROM sonarqube:community

USER root
COPY --chown=sonarqube:sonarqube sonarqube-data/ /opt/sonarqube/data/
COPY --chown=sonarqube:sonarqube sonarqube-extensions/ /opt/sonarqube/extensions/
USER sonarqube
