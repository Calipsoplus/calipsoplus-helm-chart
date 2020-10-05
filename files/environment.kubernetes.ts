export const environment = {
  production: false,
  servers: {
    api: {
      url: 'backend.calipsoplus.svc.cluster.local',
      basehref: 'services/'
    },
    guacamole: {
      integrated_remote_desktop_viewer : {
        enabled : false, // if true, the guacamole.url will be ignored as it isn't needed
        security: false,
        ignore_cert: true,
        disable_auth: true,
        cluster_url : 'cluster.local', // the server or cluster which contains all of the docker/kubernetes containers
        websocket_server : 'ws://java-server.cluster.local:8080/ws'
      },
      url: '/guac/'
    },
    jupyterhub: {
      enabled: true,
      url: 'https://eosc-pan-jhub.desy.de'
    }
  },
  auth: {
    oidc: {
      enabled: true,
      url: 'https://keycloak.desy.de/auth/realms/kubernetes/protocol/openid-connect/auth'
    },
    useroffice: {
      enabled: true,
      url: 'https://door.desy.de'
    }
  },
  frontend: {
    url: 'https://calipsoplus.desy.de/',
    facilityLogo: 'assets/images/desy-logo.jpg'
  },
  env: 'kubernetes'
};
