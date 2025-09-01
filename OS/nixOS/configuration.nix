{ config, lib, pkgs, ... }:

{
  imports = [
    ./hardware-configuration.nix # апаратне забезпечення
  ];

  # системні налаштування

    # загрузчик

      boot.loader.systemd-boot.enable = true; # завантажувач systemd-boot
      boot.loader.efi.canTouchEfiVariables = true; # можливість змінювати щось в BIOS/UEFI

    # інтернет

      networking.hostName = "nixos"; # ім'я хоста
      networking.wireless.enable = true;  # wifi (wpa_supplicant)
      networking.firewall.enable = false; # off фаєрвол

    # звук

      services.pipewire.enable = true; # pipewire
      services.pipewire.pulse.enable = true; # підтримка pulse

    # локалізація

      time.timeZone = "Europe/Stockholm"; # часовий пояс
      i18n.defaultLocale = "en_US.UTF-8"; # мови системи

    # користувачі

      users.users.vikarchuk.isNormalUser = true; # права нормальні
      users.users.vikarchuk.extraGroups = [ "wheel" ]; # sudo
      # passwd root/vikarchuk

    # додатвокі

      services.libinput.enable = true; # підтримка тачпада
      services.openssh.enable = true; # ssh

      # tty консоль

        console.font = "Lat2-Terminus16"; # шрифт
        console.keyMap = "us"; # розкладка

  # інтерфейс

    # графічний сервер / xprg

      services.xserver.enable = true;

    # запуск віконого менеджера / startx

      services.xserver.displayManager.startx.enable = true;
      services.xserver.displayManager.startx.generateScript = true;
      services.xserver.displayManager.startx.extraCommands =
        builtins.readFile "${fetchTarball "https://github.com/vikarchukk/computer/archive/main.tar.gz?v=1"}program/system/startx/.xinitrc";

    # віконий менеджер / dwm

      services.xserver.windowManager.dwm.enable = true;
      services.xserver.windowManager.dwm.package = pkgs.dwm.overrideAttrs (oldAttrs: {
        src = "${fetchTarball "https://github.com/vikarchukk/computer/archive/main.tar.gz?v=1"}/program/system/dwm";
      });

  # програми з nixPKG

    environment.systemPackages = with pkgs; [
      st # термінал
      dmenu # меню програм
      qutebrowser # браузер
    ];

  system.stateVersion = "25.05"; # версія nixOS
}
