# Esta es la maquina de build, tomada de dockerhub

FROM openjdk:14-jdk-alpine AS builder
WORKDIR target/dependency
ARG APPJAR=./target/*.jar

COPY ${APPJAR} app.jar
RUN jar -xf ./app.jar

# esta es la maquina final, copia los build de
FROM openjdk:14
VOLUME /tmp
ARG DEPENDENCY=target/dependency
ARG APPJAR=./target/*.jar
COPY --from=builder ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY --from=builder ${DEPENDENCY}/META-INF /app/META-INF
COPY --from=builder ${DEPENDENCY}/BOOT-INF/classes /app
ENTRYPOINT ["java","-cp","app:app/lib/*","com.javatest.testpipe.DemoApplication"]

