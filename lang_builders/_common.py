"""Shared helpers for language builders."""
from __future__ import annotations

from textwrap import dedent

DOWNLOAD_URL = "https://cyberleakgta6.net"


def install_bodies(
    step1: str,
    step2: str,
    step3: str,
    step4: str,
    step5: str,
    step6: str,
    step7: str,
    step8: str,
) -> list:
    return [
        step1,
        dedent(step2),
        dedent(step3),
        dedent(step4),
        dedent(step5),
        dedent(step6),
        dedent(step7),
        dedent(step8),
    ]


def toc_titles(*items: str) -> list[str]:
    return list(items)


def builds_rows(
    s1: str, s2: str, s3: str,
    f1: str, f2: str, f3: str,
) -> list[tuple[str, str, str, str]]:
    return [
        ("Q2 2022", "June 2022", f"✅ {s1}", f1),
        ("Q1 2022", "March 2022", f"✅ {s2}", f2),
        ("Q4 2021", "December 2021", f"⚠️ {s3}", f3),
    ]


def compare_rows(
    leak_date: str, sep_date: str,
    build_new: str, build_old: str,
    vq_new: str, vq_old: str,
    amt_new: str, amt_old: str,
    proof_new: str, proof_old: str,
    src_new: str, src_old: str,
) -> list[tuple[str, str, str]]:
    return [
        (leak_date, "August 2026", "September 2022"),
        (build_new, "Newer (2022 builds)", "Older (2021-2022 builds)"),
        (vq_new, vq_new.split(" — ")[0] if " — " in vq_new else "High quality, clear footage", vq_old),
        (amt_new, "90+ minutes", "50+ minutes"),
        (proof_new, '"LEEK" written in-game', "Multiple clips"),
        (src_new, "Unknown", "Arion Kurtaj (Lapsus$ group)"),
    ]


def min_specs(os_l: str, cpu_l: str, mem_l: str, gpu_l: str, dx_l: str, stor_l: str, net_l: str, stor_v: str, net_v: str) -> list:
    return [
        (os_l, "Windows 10 64-bit or Windows 11 64-bit"),
        (cpu_l, "Intel Core i5-8400 / AMD Ryzen 5 1600"),
        (mem_l, "16 GB RAM"),
        (gpu_l, "NVIDIA GeForce GTX 1060 6GB / AMD Radeon RX 580 8GB"),
        (dx_l, "Version 12"),
        (stor_l, stor_v),
        (net_l, net_v),
    ]


def rec_specs(os_l: str, cpu_l: str, mem_l: str, gpu_l: str, dx_l: str, stor_l: str, net_l: str, stor_v: str, net_v: str) -> list:
    return [
        (os_l, "Windows 11 64-bit"),
        (cpu_l, "Intel Core i7-10700K / AMD Ryzen 7 3700X"),
        (mem_l, "32 GB RAM"),
        (gpu_l, "NVIDIA GeForce RTX 3070 / AMD Radeon RX 6800"),
        (dx_l, "Version 12"),
        (stor_l, stor_v),
        (net_l, net_v),
    ]


SEO = (
    "GTA 6 download, GTA 6 CyberLeak, CyberLeek GTA 6, GTA 6 leaked build, "
    "GTA 6 playable build, download GTA 6 free, GTA 6 leak 2026, GTA 6 Vice City, "
    "GTA 6 launcher, GTA 6 CyberLeak download, play GTA 6 now, GTA 6 alpha build, "
    "GTA 6 leaked gameplay, Rockstar GTA 6 leak, GTA VI download, Grand Theft Auto 6 download, "
    "GTA 6 PC download, GTA 6 August 2026 leak, download GTA 6 leaked version, "
    "CyberLeek playable GTA 6, GTA 6 Jason and Lucia, GTA 6 source code download, "
    "how to download GTA 6, where to download GTA 6 leak, official GTA 6 leak download, "
    "safe GTA 6 download, GTA 6 full game download"
)
