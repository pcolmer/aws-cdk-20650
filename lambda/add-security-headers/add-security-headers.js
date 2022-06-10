// https://aws.amazon.com/blogs/networking-and-content-delivery/adding-http-security-headers-using-lambdaedge-and-amazon-cloudfront/
// https://www.savjee.be/2018/05/Content-security-policy-and-aws-s3-cloudfront/
'use strict';

// Trigger update

exports.handler = (event, context, callback) => {
    //Get contents of response
    const response = event.Records[0].cf.response;
    const headers = response.headers;

    // Set new headers
    headers['strict-transport-security'] = [{
        key: 'Strict-Transport-Security',
        // 1 year (365.25 days) plus one second
        value: "max-age=31557601; preload"
    }];
    headers['x-content-type-options'] = [{
        key: 'X-Content-Type-Options',
        value: "nosniff"
    }];

    for (const key in event.headers) {
        headers[key.toLowerCase()] = event.headers[key];
    }
    event.headers = headers;

    callback(null, response);
};
