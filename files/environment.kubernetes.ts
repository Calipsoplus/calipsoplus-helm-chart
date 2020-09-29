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
      enabled: true,
      url: 'https://example.com/oidc/authenticate'
    },
    useroffice: {
      enabled: false,
      url: 'https://USEROFFICE.URL'
   }
  },
  frontend: {
    url: 'https://calipsoplus.desy.de/',
    facilityLogo: 'assets/images/logo.jpg'
  },
  env : 'kubernetes'
};
