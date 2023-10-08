import fs from 'fs';

export const server = {
    host: '0.0.0.0',
    https: {
        cert: fs.readFileSync('/etc/ssl/certs/ssl-cert-snakeoil.pem'),
        key: fs.readFileSync('/etc/ssl/private/ssl-cert-snakeoil.key'),
    },
};
