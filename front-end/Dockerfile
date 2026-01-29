# ---------- Étape 1 : build ----------
FROM node:20-alpine AS build

WORKDIR /app

# Installer les dépendances
COPY package.json package-lock.json ./
RUN npm ci

# Copier le reste du code
COPY . .

CMD ["npm", "run", "dev", "--", "--host"]

# Build Vite
#RUN npm run build


# # ---------- Étape 2 : serveur web ----------
# FROM nginx:alpine

# # Supprimer la config par défaut
# RUN rm /etc/nginx/conf.d/default.conf

# # Ajouter notre config Nginx
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# # Copier le build Vite
# COPY --from=build /app/dist /usr/share/nginx/html

# EXPOSE 80

# CMD ["nginx", "-g", "daemon off;"]
