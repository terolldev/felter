class AAA(discord.ui.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @discord.ui.button(label="norm", style=discord.ButtonStyle.blurple)
    async def norm(self, _, interaction):
        await interaction.response.send_message("norm")

    @discord.ui.button(label="eph", style=discord.ButtonStyle.blurple)
    async def eph(self, _, interaction):
        await interaction.response.send_message("eph", view=self, ephemeral=True)

await _ctx.send("A", view=AAA())
