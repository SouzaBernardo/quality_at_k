FROM sonarqube:community

USER root
COPY --chown=sonarqube:sonarqube sonar-data/sonarqube-data/ /opt/sonarqube/data/
COPY --chown=sonarqube:sonarqube sonar-data/sonarqube-extensions/ /opt/sonarqube/extensions/
USER sonarqube
