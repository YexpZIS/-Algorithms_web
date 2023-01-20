async function doRequest(url, data) {
    const resopnse = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    return resopnse.json()
}