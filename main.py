import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        content_json = file.read()
        content = json.loads(content_json)

        for key, value in content.items():
            guild = None
            if value["guild"] is not None:
                guild, guild_bool = Guild.objects.get_or_create(
                    name=value["guild"]["name"],
                    defaults={
                        "description": value["guild"]["description"],
                    },
                )

            race, bool_value = Race.objects.get_or_create(
                name=value["race"]["name"],
                defaults={
                    "description": value["race"]["description"],
                },
            )

            for skill_data in value["race"]["skills"]:
                Skill.objects.get_or_create(
                    name=skill_data["name"],
                    defaults={
                        "bonus": skill_data["bonus"],
                        "race": race,
                    },
                )

            Player.objects.get_or_create(
                nickname=key,
                defaults={
                    "email": value["email"],
                    "bio": value["bio"],
                    "race": race,
                    "guild": guild,
                },
            )


if __name__ == "__main__":
    main()
