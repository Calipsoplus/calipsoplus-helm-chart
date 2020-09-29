export const environment = {
  production: true,
  servers: {
    api: {
      url: 'https://calipsobackend.domain.tld/',
      basehref: 'calipsoplus-services/'
    },
    guacamole: {
      url: 'https://calipsoplus.desy.de/gacces/'
    },
    jupyterhub: {
      enabled: true,
      url: 'https://jupyter.example.com'
    }
  },
  auth: {
    oidc: {
      enabled: {{ .Values.calipsoplus.oidc.enabled }},
      url: {{ .Values.calipsoplus.oidc.url | quote }}
    },
    useroffice: {
      enabled: false,
      url: 'https://USEROFFICE.URL'
   }
  },
  frontend: {
    url: {{ .Values.calipsoplus.frontend.url | quote }},
    facilityLogo: 'assets/images/logo.jpg'
  },
  env : 'kubernetes'
};
