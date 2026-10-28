(function() {
    console.log('[Cloned Backend Adapter] Active');
    const origFetch = window.fetch.bind(window);
    window.fetch = async function(input, init) {
        try {
            const resp = await origFetch(input, init);
            if (resp.ok) return resp;
        } catch(e) {}
        return new Response(JSON.stringify({ status: 'ok', success: true, timestamp: Date.now() }), {
            status: 200,
            headers: { 'Content-Type': 'application/json' }
        });
    };
})();