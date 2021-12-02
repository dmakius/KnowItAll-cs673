function deletePlayer(playerId) {
    fetch('/delete-player', {
        method: "POST",
        body: JSON.stringify({
            playerId: playerId
        }),
    }).then((_res) => {
        window.location.href = "admin/test-feature";
    })
}