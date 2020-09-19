FROM node:10.15.0  as ui-builder
RUN mkdir /app && mkdir -p /app/dist && mkdir -p /app/node_modules
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./package.json /app/package.json
RUN npm install --allow-root && \
    npm install -g @vue/cli
COPY . /app
RUN npm run build

# production environment
FROM nginx
COPY --from=ui-builder /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 8001

CMD ["nginx", "-g", "daemon off;"]